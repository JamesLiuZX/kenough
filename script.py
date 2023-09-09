import replicate
output = replicate.run(
 "jagilley/controlnet-depth2img:922c7bb67b87ec32cbc2fd11b1d5f94f0ba4f5519c4dbd02856376444127cc60",
input={"strength":0.9,"a_prompt":"Best quality, extremely detailed","structure":"lineart","image": open("/Users/rachpradhan/Desktop/condensation/00012.png", "rb"),"prompt":"impasto painting, in the style of Chaim Soutine, minimal"}
)
print(output)

# Download the link from output[1] and save it to the computer
link = output[1]
# Code to download the link and save it to the computer goes here
import urllib.request

image_path = "/Users/rachpradhan/Desktop/condensation/2.png"
urllib.request.urlretrieve(link, image_path)

# import os
# import replicate

# folder_path = "/Users/rachpradhan/Desktop/condensation/script.py"
# for filename in os.listdir(folder_path):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         image_path = os.path.join(folder_path, filename)
#         output = replicate.run(
#             "jagilley/controlnet-depth2img:922c7bb67b87ec32cbc2fd11b1d5f94f0ba4f5519c4dbd02856376444127cc60",
#             input={"image": open(image_path, "rb"), "prompt":"turn this into an anime animation"}
#         )
#         print(output)
