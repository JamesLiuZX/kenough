import replicate
output = replicate.run(
    "google-research/frame-interpolation:4f88a16a13673a8b589c18866e540556170a5bcb2ccdc12de556e800e9456d3d",
    input={"frame1": open("/Users/rachpradhan/Desktop/condensation/1.png", "rb"), "frame2":open("/Users/rachpradhan/Desktop/condensation/2.png", "rb")}
)
print(output)