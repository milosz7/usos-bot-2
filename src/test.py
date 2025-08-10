import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "mps"  # the device to load the model onto

model_name = "speakleash/Bielik-1.5B-v3.0-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.bfloat16)
# if tokenizer.pad_token is None:
#     tokenizer.pad_token = tokenizer.eos_token  # Set pad token to EOS token
print(model.device)
messages = [
    # {
    #     "role": "system",
    #     "content": "Odpowiadaj na pytania w języku polskim. Musisz zawsze odpowiedzieć cokolwiek.",
    # },
    {"role": "user", "content": "Kim jesteś?"},
    # {
    #     "role": "user",
    #     "content": "Jak zarejestrować się do grupy zajęciowej w USOSweb? Na podstawie poniższego tekstu odpowiedz na pytanie: Jak się zarejestrować do grupy: 1. Zaloguj się do USOSweb 2. Wybierz zakładkę DLA STUDENTÓW 3. W lewym menu wybierz żetonowe -> rejestracje 4. Z listy rejestracji wybierz odpowiednią. 5. Kliknij w odpowiednią nazwę przedmiotu, na który się rejestrujesz. 6. Rozwinie się lista z ",
    #     # "content": "Jak zarejestrować się do grupy zajęciowej w USOSweb?",
    # },
    # {"role": "user", "content": "Która jest najcieplejsza?"},
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", tokenize=True)
# attention_mask = (input_ids != tokenizer.pad_token_id).int().to(device)
model_inputs = input_ids.to(device)
model.to(device)

print("Odpowiadam....")
generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=False)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
