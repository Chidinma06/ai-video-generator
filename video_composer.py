import os
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip, vfx
from PIL import Image

def resize_image(image_path, target_size=(720, 1280)):
    img = Image.open(image_path).convert("RGB")
    img.thumbnail(target_size, Image.LANCZOS)
    background = Image.new("RGB", target_size, (0, 0, 0))
    offset = (
        (target_size[0] - img.width) // 2,
        (target_size[1] - img.height) // 2
    )
    background.paste(img, offset)
    background.save(image_path)

def compose_video(image_folder, audio_file, business_name="", output_file="final_video.mp4"):
    audio = AudioFileClip(audio_file)
    duration = audio.duration

    images = sorted([
        os.path.join(image_folder, f)
        for f in os.listdir(image_folder)
        if f.endswith(".jpg")
    ])

    for img_path in images:
        resize_image(img_path)

    clip_duration = duration / len(images)

    clips = []
    for img in images:
        clip = ImageClip(img).with_duration(clip_duration).with_effects([vfx.FadeIn(0.5), vfx.FadeOut(0.5)])
        clips.append(clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip = final_clip.with_audio(audio)

    if business_name:
        txt_clip = TextClip(
            text=business_name,
            font_size=70,
            color="white",
            font="C:/Windows/Fonts/arial.ttf",
            stroke_color="black",
            stroke_width=2,
            size=(1080, None)
        ).with_duration(duration).with_position(("center", 1750))
        final_clip = CompositeVideoClip([final_clip, txt_clip])

    final_clip.write_videofile(output_file, fps=24, threads=4, preset="ultrafast")
    print("Video saved!")