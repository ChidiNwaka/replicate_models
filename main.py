import sys 
import replicate
from datetime import datetime

def generateImage(prompt):
    unique_filename = "output" + " - " + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={
            "prompt": prompt
        }
    )

    with open(f'{unique_filename}', "wb") as f:
        f.write(output[0].read())
    
    print(f"Image saved as output.png")

def generateSentence(prompt):
    # The meta/llama-2-7b model can stream output as it's running.
    for event in replicate.run(
        "meta/llama-2-7b",
        input={
            "prompt": prompt,
            "max_tokens": 512,
        },
    ):
        print(str(event), end="")

if __name__=="__main__":
    # generateSentence("Write a four sentence of How is it living in Lagos, Nigeria")
    prompt = input("Please enter a prompt for an image: ")
    generateImage(prompt)

