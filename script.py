import replicate
import os
import urllib.request

input_folder = "/Users/rachpradhan/Desktop/condensation/input_images"
output_folder = "/Users/rachpradhan/Desktop/condensation/output_links"

input_images = []
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_images.append(open(os.path.join(input_folder, filename), "rb"))

output_links = []
for image in input_images:
    output = replicate.run(
        "jagilley/controlnet-depth2img:922c7bb67b87ec32cbc2fd11b1d5f94f0ba4f5519c4dbd02856376444127cc60",
        input={"strength":0.9,"a_prompt":"Best quality, extremely detailed","structure":"lineart","image": image,"prompt":"impasto painting, in the style of Chaim Soutine, minimal"}
    )
    output_links.append(output[1])

for index, link in enumerate(output_links): 
    # Generate a new filename based on the index
    new_filename = f"output_image_{index}.png"
    urllib.request.urlretrieve(link, os.path.join(output_folder, new_filename))

print("All images processed and links saved successfully.")
