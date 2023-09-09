import replicate
output = replicate.run(
 "jagilley/controlnet-depth2img:922c7bb67b87ec32cbc2fd11b1d5f94f0ba4f5519c4dbd02856376444127cc60",
input={"seed":13666,"strength":0.9,"a_prompt":"Best quality, extremely detailed","structure":"lineart","image": open("/Users/rachpradhan/Desktop/condensation/00001.png", "rb"),"prompt":"Photo of a sci-fi handsome guy with silver hair, photorealistic, in the style of Franciszek Starowieyski. He has a white porcelain sci-fi appearance with machine aesthetics reminiscent of mecha designs. The image should be in 32k UHD resolution, with a color palette dominated by dark white, azure, silver, and hints of pink. The background should depict a science fiction city. His hair should have a shiny silver appearance, and the artwork should capture him from the waist up, resembling an oil painting in the manner of Hans Zatzka."}
)
print(output)

# Download the link from output[1] and save it to the computer
link = output[1]
# Code to download the link and save it to the computer goes here
import urllib.request

image_path = "/Users/rachpradhan/Desktop/condensation/2.png"
urllib.request.urlretrieve(link, image_path)


