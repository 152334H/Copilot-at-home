from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

from packaging import version
assert version.parse(transformers.__version__) >= version.parse("4.24.0")

print('loading model...')
'''
tokenizer = AutoTokenizer.from_pretrained("NinedayWang/PolyCoder-2.7B")
model = AutoModelForCausalLM.from_pretrained("NinedayWang/PolyCoder-2.7B", pad_token_id=tokenizer.eos_token_id).to('cuda')
'''
MODEL_NAME = "Salesforce/codegen-2B-mono"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16).to('cuda')
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def predict(prompt: str, max_len=128, penalty_alpha=0.4, top_k=3):
    print('predicting:', prompt.split('\n')[0][:50], '...')
    inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
    result = model.generate(**inputs, max_length=max_len, penalty_alpha=penalty_alpha, top_k=top_k)
    #input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')
    #result = model.generate(input_ids, max_length=max_len, penalty_alpha=penalty_alpha, top_k=top_k)
    assert len(result) == 1
    return tokenizer.decode(result[0], truncate_before_pattern=[r"\n\n^#", "^'''", "\n\n\n"])

if __name__ == '__main__':
    # manual testing from a terminal
    while 1:
        lines = []
        while (p:=input('> ')) != 'END':
            lines.append(p)
        print(predict('\n'.join(lines)))
