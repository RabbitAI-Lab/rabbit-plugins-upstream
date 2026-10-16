#!/usr/bin/env python3
"""Free image generation via Pollinations.ai with retry logic for rate limits."""

import argparse
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

OUTPUT_DIR = os.path.expanduser("~/.openclaw/media/pollinations-image")
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds between retries


def generate(prompt: str, width: int = 1024, height: int = 1024, nologo: bool = True, seed: int | None = None) -> str:
    """Generate an image and return the file path. Retries on rate limit (402)."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    params = {"width": width, "height": height, "nologo": "true"}
    if seed is not None:
        params["seed"] = str(seed)

    query = urllib.parse.urlencode(params)
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?{query}"

    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = resp.read()
                if len(data) < 100:
                    raise ValueError("Response too small, likely an error page")

            timestamp = int(time.time())
            output_path = os.path.join(OUTPUT_DIR, f"img_{timestamp}.jpg")
            with open(output_path, "wb") as f:
                f.write(data)
            return output_path

        except urllib.error.HTTPError as e:
            if e.code == 402 and attempt < MAX_RETRIES - 1:
                wait = RETRY_DELAY * (attempt + 1)
                print(f"Rate limited (402), retrying in {wait}s... (attempt {attempt + 1}/{MAX_RETRIES})", file=sys.stderr)
                time.sleep(wait)
            else:
                raise
        except Exception as e:
            if attempt < MAX_RETRIES - 1:
                wait = RETRY_DELAY * (attempt + 1)
                print(f"Error: {e}, retrying in {wait}s... (attempt {attempt + 1}/{MAX_RETRIES})", file=sys.stderr)
                time.sleep(wait)
            else:
                raise

    raise RuntimeError(f"Failed to generate image after {MAX_RETRIES} attempts")


def main():
    parser = argparse.ArgumentParser(description="Generate AI images via Pollinations.ai (free, no key)")
    parser.add_argument("prompt", help="Image description")
    parser.add_argument("--width", "-w", type=int, default=1024, help="Image width (default: 1024)")
    parser.add_argument("--height", "-H", type=int, default=1024, help="Image height (default: 1024)")
    parser.add_argument("--nologo", action="store_true", default=True, help="Remove watermark")
    parser.add_argument("--seed", "-s", type=int, default=None, help="Fixed seed for reproducibility")
    args = parser.parse_args()

    path = generate(args.prompt, args.width, args.height, args.nologo, args.seed)
    print(path)


if __name__ == "__main__":
    main()
