#!/usr/bin/env python3

import base64
import json
import os
import shutil
import subprocess
import sys


def fail(message, code=1):
    print(f"speak: {message}", file=sys.stderr)
    raise SystemExit(code)


text = " ".join(sys.argv[1:]).strip()

if not text:
    fail('uso: run.py "testo da pronunciare"', 2)


openclaw = shutil.which("openclaw")

if not openclaw:
    fail("binary 'openclaw' non trovato nel PATH")


params = json.dumps(
    {
        "text": text,
        "outputFormat": "wav",
    },
    ensure_ascii=False,
)


try:
    proc = subprocess.run(
        [
            openclaw,
            "gateway",
            "call",
            "talk.speak",
            "--params",
            params,
            "--json",
        ],
        capture_output=True,
        text=True,
        timeout=60,
    )
except subprocess.TimeoutExpired:
    fail("talk.speak ha superato il timeout")


if proc.returncode != 0:
    message = proc.stderr.strip() or proc.stdout.strip()
    fail(f"talk.speak fallito: {message}")


try:
    payload = json.loads(proc.stdout)
except json.JSONDecodeError as exc:
    fail(f"risposta JSON non valida da OpenClaw: {exc}")


result = payload.get("result") if isinstance(payload, dict) else None
if not isinstance(result, dict):
    result = payload


if not isinstance(result, dict) or not result.get("audioBase64"):
    fail("talk.speak non ha restituito audioBase64")


try:
    audio = base64.b64decode(result["audioBase64"], validate=True)
except Exception as exc:
    fail(f"audio Base64 non valido: {exc}")


if not audio:
    fail("talk.speak ha restituito audio vuoto")


output_format = result.get("outputFormat")

if output_format and output_format != "wav":
    fail(f"formato audio inatteso: {output_format}")


aplay = shutil.which("aplay")

if not aplay:
    fail("binary 'aplay' non trovato")


command = [aplay]

device = os.environ.get("SPEAK_ALSA_DEVICE", "").strip()
if device:
    command += ["-D", device]

command.append("-")


player = subprocess.run(
    command,
    input=audio,
)

if player.returncode != 0:
    fail(f"aplay terminato con codice {player.returncode}")
