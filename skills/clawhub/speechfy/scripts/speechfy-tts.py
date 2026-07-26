#!/usr/bin/env python3
"""
Speechify TTS — Multi-provider Text-to-Speech

Generates audio from text using Speechify API (primary) with fallback to
Edge TTS (Microsoft). Outputs .ogg (Opus) ready for voice messages.

Usage:
  # Basic — text + output path
  python3 scripts/speechfy-tts.py "Hello, world!" /tmp/hello.ogg

  # With environment variables for configuration
  SPEECHIFY_VOICE=bruno python3 scripts/speechfy-tts.py "Texto" /tmp/saida.ogg

  # Force fallback to Edge TTS
  SPEECHIFY_API_KEY="" python3 scripts/speechfy-tts.py "Fala" /tmp/saida.ogg
"""

import sys, os, json, base64, subprocess, urllib.request, tempfile

# ── Config via environment variables ──────────────────
SPEECHIFY_VOICE = os.environ.get("SPEECHIFY_VOICE", "cristiane")
SPEECHIFY_MODEL = os.environ.get("SPEECHIFY_MODEL", "simba-multilingual")
SPEECHIFY_LANG  = os.environ.get("SPEECHIFY_LANG", "pt-BR")
EDGE_VOICE      = os.environ.get("EDGE_TTS_VOICE", "pt-BR-FranciscaNeural")
OUTPUT_DEFAULT  = os.environ.get("SPEECHIFY_OUTPUT", "/tmp/speech-output.ogg")
VAULT_ITEM      = os.environ.get("SPEECHIFY_VAULT_ITEM", "speechfy_key")
# ──────────────────────────────────────────────────────

def log(msg):
    print(f"[speechfy-tts] {msg}", file=sys.stderr)

def get_api_key():
    """Resolve Speechify API key: env var first, then vault-resolver (optional)."""
    key = os.environ.get("SPEECHIFY_API_KEY", "")
    if key:
        return key

    vault_resolver = os.environ.get("VAULT_RESOLVER", "/opt/data/bin/vault-resolver")
    if os.path.isfile(vault_resolver):
        try:
            proc = subprocess.run(
                [vault_resolver, "resolve"],
                input=json.dumps({"ids": [VAULT_ITEM]}).encode(),
                capture_output=True, timeout=20
            )
            result = json.loads(proc.stdout.decode())
            return result.get("values", {}).get(VAULT_ITEM, "")
        except Exception as e:
            log(f"vault-resolver error: {e}")

    return ""

def try_speechify(text, output_path):
    """Try Speechify API. Returns True on success."""
    key = get_api_key()
    if not key:
        log("Speechify: no API key found — skipping")
        return False

    payload = {
        "input": text,
        "voice_id": SPEECHIFY_VOICE,
        "audio_format": "mp3",
        "model": SPEECHIFY_MODEL,
        "language": SPEECHIFY_LANG
    }

    req = urllib.request.Request(
        "https://api.speechify.ai/v1/audio/speech",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        audio_b64 = data.get("audio_data", "")
        if not audio_b64:
            log("Speechify: response missing audio_data")
            return False
        chars = data.get("billable_characters_count", 0)
        log(f"Speechify OK: {len(audio_b64)}b base64, {chars} chars")

        mp3_tmp = output_path + ".tmp.mp3"
        with open(mp3_tmp, "wb") as f:
            f.write(base64.b64decode(audio_b64))
        subprocess.run(
            ["ffmpeg", "-y", "-i", mp3_tmp,
             "-c:a", "libopus", "-b:a", "32k",
             output_path],
            capture_output=True, timeout=30
        )
        os.remove(mp3_tmp)
        return os.path.getsize(output_path) > 1000

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(f"Speechify HTTP {e.code}: {body[:200]}")
        return False
    except Exception as e:
        log(f"Speechify error: {e}")
        return False

def try_edge_tts(text, output_path):
    """Fallback via Edge TTS (Microsoft)."""
    edge_cmd = os.environ.get("EDGE_TTS_CMD", "edge-tts")
    try:
        subprocess.run(
            [edge_cmd, "--voice", EDGE_VOICE,
             "--text", text,
             "--write-media", output_path],
            capture_output=True, timeout=60, check=True
        )
        if os.path.getsize(output_path) > 1000:
            log(f"Edge TTS OK ({EDGE_VOICE})")
            return True
        return False
    except Exception as e:
        log(f"Edge TTS error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <text> [output.ogg]", file=sys.stderr)
        sys.exit(1)

    text = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else OUTPUT_DEFAULT

    log(f"Text: {text[:80]}...")
    log(f"Output: {output}")
    log(f"Primary: Speechify ({SPEECHIFY_VOICE})")
    log(f"Fallback: Edge TTS ({EDGE_VOICE})")

    if try_speechify(text, output):
        print(output)
        sys.exit(0)

    log("Fallback: Edge TTS...")
    if try_edge_tts(text, output):
        print(output)
        sys.exit(0)

    log("FAILED: No TTS provider worked")
    sys.exit(1)

if __name__ == "__main__":
    main()
