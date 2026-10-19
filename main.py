import os
from script_generator import generate_script
from voice_generator import generate_voice
from visual_fetcher import fetch_images
from video_composer import compose_video

business_name = "Adaeze Fabrics"
description = "A fabric and fashion store selling Ankara and lace materials"
target_audience = "Nigerian women aged 20 to 45"
tone = "warm and energetic"
keyword = "African Ankara fabric fashion Nigeria"

print("Generating script...")
script = generate_script(business_name, description, target_audience, tone)
print(script)
print("\nGenerating voiceover...")
generate_voice(script)

import os
if not os.listdir("assets/images"):
    print("\nFetching images...")
    fetch_images(keyword)
else:
    print("\nUsing existing images...")

print("\nComposing video...")
compose_video("assets/images", "voiceover.mp3", business_name=business_name)

print("\nDone! Your video is ready: final_video.mp4")