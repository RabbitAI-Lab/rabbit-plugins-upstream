"""Audio extraction and ASR helpers for video-downloader."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import uuid
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

SILICONFLOW_TRANSCRIPTION_URL = "https://api.siliconflow.cn/v1/audio/transcriptions"
SILICONFLOW_DEFAULT_MODEL = "FunAudioLLM/SenseVoiceSmall"

# whisper.cpp command and model paths are configurable via environment variables.
# Keep user-specific locations out of source control.
WHISPER_CPP_BIN = os.environ.get("WHISPER_CPP_BIN", "").strip()
WHISPER_CPP_MODEL = os.environ.get("WHISPER_CPP_MODEL", "")


def run_asr(
    video_path: Path,
    output_dir: Path,
    *,
    backend: str = "auto",
    model: str = "auto",
    language: str = "auto",
    prompt: str | None = None,
    max_seconds: float | None = None,
) -> dict:
    if backend == "none":
        return _asr_result(
            status="skipped",
            backend="none",
            model=None,
            language=language,
            prompt=prompt,
        )

    try:
        selected_backend = _select_backend(backend)
    except RuntimeError as exc:
        requested_model = (
            _resolve_model(backend, model)
            if backend in {"whisper_cpp", "whisper", "siliconflow"}
            else None
        )
        return _asr_result(
            status="failed",
            backend=backend,
            model=requested_model,
            language=language,
            prompt=prompt,
            error=str(exc),
        )

    if selected_backend is None:
        return _asr_result(
            status="pending",
            backend=backend,
            model=None,
            language=language,
            prompt=prompt,
            error=(
                "No ASR backend is available. "
                "Add whisper-cli to PATH or set WHISPER_CPP_BIN and WHISPER_CPP_MODEL, "
                "make the openai-whisper CLI available on PATH, or set SILICONFLOW_API_KEY. "
                "Use --asr none to skip transcription. No software is installed automatically."
            ),
        )

    # Choose audio format per backend
    if selected_backend == "siliconflow":
        audio_path = output_dir / "audio.mp3"
    elif selected_backend == "whisper_cpp":
        audio_path = output_dir / "audio.wav"
    else:
        audio_path = output_dir / "audio.m4a"

    transcript_path = output_dir / "transcript.txt"
    srt_path = output_dir / "transcript.srt"
    whisper_json_path = output_dir / "transcript.whisper.json"
    whisper_cpp_json_path = output_dir / "transcript.whisper_cpp.json"
    siliconflow_json_path = output_dir / "transcript.siliconflow.json"
    resolved_model = _resolve_model(selected_backend, model)
    result_srt: Path | None = None
    raw_json_path: Path | None = None

    try:
        extract_audio(video_path, audio_path, max_seconds=max_seconds)

        if selected_backend == "siliconflow":
            transcribe_with_siliconflow(
                audio_path,
                transcript_path,
                siliconflow_json_path,
                model=resolved_model,
            )
            raw_json_path = siliconflow_json_path
        elif selected_backend == "whisper_cpp":
            result_srt = transcribe_with_whisper_cpp(
                audio_path,
                output_dir,
                transcript_path,
                srt_path,
                model_path=resolved_model,
                language=language,
                prompt=prompt,
            )
            raw_json_path = whisper_cpp_json_path
        else:
            result_srt = transcribe_with_whisper(
                audio_path,
                output_dir,
                transcript_path,
                srt_path,
                whisper_json_path,
                model=resolved_model,
                language=language,
                prompt=prompt,
            )
            raw_json_path = whisper_json_path
    except RuntimeError as exc:
        return _asr_result(
            status="failed",
            backend=selected_backend,
            model=resolved_model,
            language=language,
            prompt=prompt,
            audio_path=audio_path,
            error=str(exc),
        )

    return _asr_result(
        status="done",
        backend=selected_backend,
        model=resolved_model,
        language=language,
        prompt=prompt,
        audio_path=audio_path,
        transcript_path=transcript_path,
        srt_path=result_srt,
        raw_json_path=raw_json_path,
    )


def _asr_result(
    *,
    status: str,
    backend: str,
    model: str | None,
    language: str,
    prompt: str | None,
    audio_path: Path | None = None,
    transcript_path: Path | None = None,
    srt_path: Path | None = None,
    raw_json_path: Path | None = None,
    error: str | None = None,
) -> dict:
    return {
        "status": status,
        "backend": backend,
        "model": model,
        "language": language,
        "prompt": prompt or default_prompt_for(language),
        "audio_path": str(audio_path) if audio_path else None,
        "transcript_path": str(transcript_path) if transcript_path else None,
        "srt_path": str(srt_path) if srt_path else None,
        "raw_json_path": str(raw_json_path) if raw_json_path else None,
        "error": error,
    }


def extract_audio(video_path: Path, audio_path: Path, *, max_seconds: float | None = None) -> None:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpeg is required for audio extraction but was not found on PATH.")

    suffix = audio_path.suffix.lower()
    command = [
        ffmpeg,
        "-y",
        "-i",
        str(video_path),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
    ]
    if suffix == ".mp3":
        command.extend(["-b:a", "64k", "-codec:a", "libmp3lame"])
    elif suffix == ".wav":
        command.extend(["-codec:a", "pcm_s16le"])
    else:
        command.extend(["-b:a", "64k"])
    if max_seconds is not None:
        command.extend(["-t", str(max_seconds)])
    command.append(str(audio_path))
    _run(command, "ffmpeg audio extraction failed")


def transcribe_with_whisper_cpp(
    audio_path: Path,
    output_dir: Path,
    transcript_path: Path,
    srt_path: Path,
    *,
    model_path: str,
    language: str,
    prompt: str | None,
) -> Path | None:
    """Transcribe using whisper.cpp (whisper-cli).

    Returns the SRT path if SRT was successfully produced, else None.
    """
    whisper_cli = _resolve_whisper_cpp_bin()
    if not whisper_cli:
        raise RuntimeError(
            "whisper-cli was not found on PATH. "
            "Set WHISPER_CPP_BIN to an executable whisper-cli path."
        )

    if not model_path:
        raise RuntimeError(
            "WHISPER_CPP_MODEL is not set. Point it to a local GGML model file."
        )
    if not os.path.isfile(model_path):
        raise RuntimeError(f"whisper.cpp model not found: {model_path}")

    # Build output prefix (without extension): whisper-cli appends .txt / .srt
    with tempfile.TemporaryDirectory(dir=str(output_dir)) as temp_dir:
        output_prefix = str(Path(temp_dir) / audio_path.stem)

        command = [
            whisper_cli,
            "--file", str(audio_path),
            "--model", model_path,
            "--output-file", output_prefix,
            "--output-txt",
            "--output-srt",
            "--no-prints",
        ]

        # Language
        if language and language.lower() == "auto":
            command.extend(["--language", "auto"])
        elif language:
            lang = _map_language_for_whisper_cpp(language)
            command.extend(["--language", lang])

        # Prompt
        initial_prompt = prompt or default_prompt_for(language)
        if initial_prompt:
            command.extend(["--prompt", initial_prompt])

        _run(command, "whisper.cpp transcription failed", timeout=3600)

        # Read generated .txt
        generated_txt = Path(f"{output_prefix}.txt")
        if not generated_txt.exists():
            raise RuntimeError("whisper.cpp finished but did not produce .txt output.")

        transcript = generated_txt.read_text(encoding="utf-8").strip()
        transcript_path.write_text(transcript + ("\n" if transcript else ""), encoding="utf-8")

        # Save minimal metadata JSON
        meta = {
            "backend": "whisper_cpp",
            "model": model_path,
            "language": language,
            "prompt": initial_prompt,
        }
        whisper_cpp_json_path = output_dir / "transcript.whisper_cpp.json"
        whisper_cpp_json_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        # Copy SRT if generated
        generated_srt = Path(f"{output_prefix}.srt")
        if not generated_srt.exists():
            raise RuntimeError("whisper.cpp finished but did not produce SRT output.")
        shutil.copy2(generated_srt, srt_path)
        return srt_path


def transcribe_with_whisper(
    audio_path: Path,
    output_dir: Path,
    transcript_path: Path,
    srt_path: Path,
    whisper_json_path: Path,
    *,
    model: str,
    language: str,
    prompt: str | None,
) -> Path:
    whisper = shutil.which("whisper")
    if not whisper:
        raise RuntimeError("whisper CLI was not found on PATH.")

    with tempfile.TemporaryDirectory(dir=str(output_dir)) as temp_dir:
        command = [
            whisper,
            str(audio_path),
            "--model",
            model,
            "--output_dir",
            temp_dir,
            "--output_format",
            "all",
            "--task",
            "transcribe",
            "--fp16",
            "False",
            "--verbose",
            "False",
        ]
        if language and language.lower() != "auto":
            command.extend(["--language", language])
        initial_prompt = prompt or default_prompt_for(language)
        if initial_prompt:
            command.extend(["--initial_prompt", initial_prompt])
        _run(command, "whisper transcription failed", timeout=3600)

        source_json = Path(temp_dir) / f"{audio_path.stem}.json"
        if not source_json.exists():
            raise RuntimeError("whisper finished but did not produce JSON output.")
        source_srt = Path(temp_dir) / f"{audio_path.stem}.srt"
        if not source_srt.exists():
            raise RuntimeError("whisper finished but did not produce SRT output.")

        data = json.loads(source_json.read_text(encoding="utf-8"))
        transcript = (data.get("text") or "").strip()
        transcript_path.write_text(transcript + ("\n" if transcript else ""), encoding="utf-8")
        shutil.copy2(source_srt, srt_path)
        data["model"] = model
        data["language_requested"] = language
        data["prompt"] = initial_prompt
        whisper_json_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return srt_path


def transcribe_with_siliconflow(
    audio_path: Path,
    transcript_path: Path,
    raw_json_path: Path,
    *,
    model: str,
) -> None:
    api_key = os.environ.get("SILICONFLOW_API_KEY")
    if not api_key:
        raise RuntimeError("SILICONFLOW_API_KEY is required for ASR backend 'siliconflow'.")

    body, content_type = _multipart_body(
        fields={"model": model},
        file_field="file",
        file_path=audio_path,
        file_content_type="audio/mpeg",
    )
    request = Request(
        SILICONFLOW_TRANSCRIPTION_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": content_type,
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=600) as response:
            response_text = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = _redact_secret(
            exc.read().decode("utf-8", errors="replace"),
            api_key,
        )
        raise RuntimeError(f"SiliconFlow transcription failed: HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        detail = _redact_secret(str(exc), api_key)
        raise RuntimeError(f"SiliconFlow transcription failed: {detail}") from exc

    try:
        data = json.loads(response_text)
    except json.JSONDecodeError as exc:
        detail = _redact_secret(response_text[:500], api_key)
        raise RuntimeError(f"SiliconFlow returned non-JSON response: {detail}") from exc

    data = _redact_secret(data, api_key)
    transcript = (data.get("text") or "").strip()
    if not transcript:
        raise RuntimeError("SiliconFlow transcription response did not include text.")
    transcript_path.write_text(transcript + "\n", encoding="utf-8")
    data["model"] = model
    raw_json_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _redact_secret(value, secret: str):
    if isinstance(value, str):
        return value.replace(secret, "[REDACTED]") if secret else value
    if isinstance(value, list):
        return [_redact_secret(item, secret) for item in value]
    if isinstance(value, dict):
        return {
            _redact_secret(key, secret): _redact_secret(item, secret)
            for key, item in value.items()
        }
    return value


def default_prompt_for(language: str) -> str | None:
    if language and language.lower() in {"chinese", "zh", "mandarin"}:
        return "请使用简体中文转写，不要使用繁体中文。保留专有名词、英文缩写和产品名称。"
    return None


# ---------------------------------------------------------------------------
# Backend selection (order matters for "auto")
# ---------------------------------------------------------------------------

def _select_backend(backend: str) -> str | None:
    if backend == "whisper_cpp":
        return _require_whisper_cpp()
    if backend == "whisper":
        return _check_whisper() or _raise_no_backend("whisper")
    if backend == "siliconflow":
        return _check_siliconflow() or _raise_no_backend("siliconflow")
    if backend == "auto":
        # Priority: whisper.cpp → openai-whisper → SiliconFlow → error
        backend_name = _check_whisper_cpp()
        if backend_name:
            return backend_name
        backend_name = _check_whisper()
        if backend_name:
            return backend_name
        backend_name = _check_siliconflow()
        if backend_name:
            return backend_name
        return None  # Nothing available — caller will report
    raise RuntimeError(f"Unsupported ASR backend: {backend}")


def _check_whisper_cpp() -> str | None:
    """Return 'whisper_cpp' if whisper.cpp is usable, else None."""
    if not _resolve_whisper_cpp_bin():
        return None
    if os.path.isfile(WHISPER_CPP_MODEL):
        return "whisper_cpp"
    return None


def _require_whisper_cpp() -> str:
    if not _resolve_whisper_cpp_bin():
        _raise_no_backend("whisper_cpp")
    if not WHISPER_CPP_MODEL:
        raise RuntimeError(
            "WHISPER_CPP_MODEL is not set. Point it to a local GGML model file."
        )
    if not os.path.isfile(WHISPER_CPP_MODEL):
        raise RuntimeError(f"whisper.cpp model not found: {WHISPER_CPP_MODEL}")
    return "whisper_cpp"


def _resolve_whisper_cpp_bin() -> str | None:
    """Resolve whisper-cli from WHISPER_CPP_BIN first, then PATH."""
    if WHISPER_CPP_BIN:
        if not os.path.isfile(WHISPER_CPP_BIN):
            raise RuntimeError(
                f"WHISPER_CPP_BIN is set but the file does not exist: {WHISPER_CPP_BIN}"
            )
        if not os.access(WHISPER_CPP_BIN, os.X_OK):
            raise RuntimeError(
                f"WHISPER_CPP_BIN is set but is not executable: {WHISPER_CPP_BIN}"
            )
        return WHISPER_CPP_BIN
    return shutil.which("whisper-cli")


def _check_whisper() -> str | None:
    """Return 'whisper' if openai-whisper CLI is usable, else None."""
    return "whisper" if shutil.which("whisper") else None


def _check_siliconflow() -> str | None:
    """Return 'siliconflow' if SILICONFLOW_API_KEY is set, else None."""
    return "siliconflow" if os.environ.get("SILICONFLOW_API_KEY") else None


def _raise_no_backend(name: str):
    msgs = {
        "whisper_cpp": (
            "whisper-cli was not found on PATH. Set WHISPER_CPP_BIN to an executable "
            "whisper-cli path and set WHISPER_CPP_MODEL to a local GGML model file. "
            "No software is installed automatically."
        ),
        "whisper": (
            "The openai-whisper 'whisper' command was not found on PATH. "
            "Configure it outside this project or choose another ASR backend. "
            "No software is installed automatically."
        ),
        "siliconflow": (
            "SILICONFLOW_API_KEY is not set. Obtain an API key from https://siliconflow.cn."
        ),
    }
    raise RuntimeError(msgs.get(name, f"Backend '{name}' is not available."))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_model(backend: str, model: str) -> str:
    if backend == "siliconflow" and model in {"auto", "base", ""}:
        return SILICONFLOW_DEFAULT_MODEL
    if backend == "whisper" and model in {"auto", ""}:
        return "base"
    if backend == "whisper_cpp":
        return WHISPER_CPP_MODEL
    return model


def _map_language_for_whisper_cpp(language: str) -> str:
    """Map user-friendly language names to whisper.cpp language codes."""
    mapping = {
        "chinese": "zh",
        "mandarin": "zh",
        "english": "en",
        "japanese": "ja",
        "korean": "ko",
        "french": "fr",
        "german": "de",
        "spanish": "es",
        "portuguese": "pt",
        "russian": "ru",
        "italian": "it",
    }
    return mapping.get(language.lower(), language)


def _multipart_body(
    *,
    fields: dict[str, str],
    file_field: str,
    file_path: Path,
    file_content_type: str,
) -> tuple[bytes, str]:
    boundary = f"----video-downloader-{uuid.uuid4().hex}"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8"),
                str(value).encode("utf-8"),
                b"\r\n",
            ]
        )
    parts.extend(
        [
            f"--{boundary}\r\n".encode("utf-8"),
            (
                f'Content-Disposition: form-data; name="{file_field}"; '
                f'filename="{file_path.name}"\r\n'
            ).encode("utf-8"),
            f"Content-Type: {file_content_type}\r\n\r\n".encode("utf-8"),
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode("utf-8"),
        ]
    )
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def _run(command: list[str], error_message: str, *, timeout: int = 600) -> None:
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or completed.stdout.strip()
        raise RuntimeError(f"{error_message}: {detail}")
