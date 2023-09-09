import subprocess, os

def video_to_photos(file_url: str):

    # FFMPEG command to split videos into photos
    command = [
    "ffmpeg",
    "-i",
    file_url,
    "-r",
    "10",
    "photos/%05d.png"
    ]

    # Run the FFmpeg command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Print any output and error messages (if any)
    print("STDOUT:", result.stdout.decode())
    print("STDERR:", result.stderr.decode())

    # Return path to photos folder
    return "photos"


def photos_to_video(file_url: str):
    # Specify the directory containing your PNG files
    working_directory = file_url

    command = [
    "ffmpeg",
    "-framerate",
    "10",
    "-pattern_type",
    "glob",
    "-i",
    "*.png",
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    "out.mp4"
    ]      

    # Change the working directory
    os.chdir(working_directory)

    # Run the FFmpeg command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Print any output and error messages (if any)
    print("STDOUT:", result.stdout.decode())
    print("STDERR:", result.stderr.decode())

    # Return path to video
    output_file_path = os.path.abspath("out.mp4")
    return output_file_path
