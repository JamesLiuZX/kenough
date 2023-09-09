import replicate
import os
import urllib.request
import concurrent.futures

input_folder = "/Users/rachpradhan/Desktop/condensation/input_images"
output_folder = "/Users/rachpradhan/Desktop/condensation/output_links2"

def process_image(image):
    print("running")
    output = replicate.run(
        "jagilley/controlnet-depth2img:922c7bb67b87ec32cbc2fd11b1d5f94f0ba4f5519c4dbd02856376444127cc60",
        input={"seed":13666,"strength":0.9,"a_prompt":"Best quality, extremely detailed","structure":"lineart","image": image,"prompt":"Photo of a sci-fi handsome guy with silver hair, photorealistic, in the style of Franciszek Starowieyski. He has a white porcelain sci-fi appearance with machine aesthetics reminiscent of mecha designs. The image should be in 32k UHD resolution, with a color palette dominated by dark white, azure, silver, and hints of pink. The background should depict a science fiction city. His hair should have a shiny silver appearance, and the artwork should capture him from the waist up, resembling an oil painting in the manner of Hans Zatzka."}
    )
    return output[1]

input_images = []
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_images.append(open(os.path.join(input_folder, filename), "rb"))

# Use ThreadPoolExecutor to process images in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    output_links = list(executor.map(process_image, input_images))

for index, link in enumerate(output_links): 
    # Generate a new filename based on the index
    new_filename = f"output_image_{index}.png"
    urllib.request.urlretrieve(link, os.path.join(output_folder, new_filename))

print("All images processed and links saved successfully.")
