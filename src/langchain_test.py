import torch
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_path = "speakleash/Bielik-4.5B-v3.0-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)

text_gen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,  # careful: 16384 might cause CUDA OOM
    do_sample=True,
    return_full_text=True,
)

llm = HuggingFacePipeline(pipeline=text_gen_pipeline)

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
    <s><|im_start|>system
    Jesteś asystentem AI. Odpowiadaj krótko, precyzyjnie i wyłącznie w języku polskim. Używaj pełnych zdań. Proces myślowy i odpowiedzi umieszczaj w tagach <think></think> i <answer></answer><|im_end|>

    <|im_start|>user
    {question}<|im_end|>
    """
)

rag_chain = (
        {"question": RunnablePassthrough()} | prompt_template | llm
)

query = "Jaki był najgorszy prezydent polski?"
response = rag_chain.invoke(query)

print(20 * "#", "\n", response)
