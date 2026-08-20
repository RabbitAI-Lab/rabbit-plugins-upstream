#!/usr/bin/env python3
"""Voiceover via Edge TTS (gratis) — da-DK-JeppeNeural som standard."""
import json, os, sys, asyncio

def main():
    if len(sys.argv) < 3:
        print("Brug: voiceover.py scenes.json audio/"); sys.exit(1)
    scenes = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    voice = os.environ.get("VOICE", "da-DK-JeppeNeural")
    try:
        import edge_tts
    except ImportError:
        print("pip install edge-tts"); sys.exit(1)
    async def gen():
        for sc in scenes:
            path = os.path.join(out, f"scene_{sc['id']:02d}.mp3")
            if os.path.exists(path):
                print(f"  findes: {path}"); continue
            tts = edge_tts.Communicate(sc["narration"], voice, rate="-5%")
            await tts.save(path)
            print(f"✅ scene {sc['id']}: {path}")
    asyncio.run(gen())
    print("Færdig.")

if __name__ == "__main__":
    main()
