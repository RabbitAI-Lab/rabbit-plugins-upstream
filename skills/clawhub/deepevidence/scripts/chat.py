#!/usr/bin/env python3
"""
DeepEvidence Chat — Medical Q&A via OpenAI-compatible API.

Usage:
    python chat.py "What are the symptoms of diabetes?"
    python chat.py "What are the symptoms of diabetes?" --user external-user-123
    python chat.py "What are follow-up treatment options?" --conversation-id abc123
    python chat.py "What are the CKD staging criteria?" --locale en
    python chat.py "请分析这张医学图片的关键信息。" --image-url https://example.com/medical-image.jpg --stream

Environment:
    DEEPEVIDENCE_API_KEY    Required. API key for authentication.
    DEEPEVIDENCE_USER_ID    Optional. Default external user ID.
"""

import os
import sys
import argparse
import json
from typing import Optional

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed. Run: pip install openai")
    sys.exit(1)

DEFAULT_TEMP_UNAVAILABLE_MSG = (
    "Temporarily unable to retrieve evidence-based results. "
    "Please try again later or consult a licensed clinician."
)


def _debug_enabled() -> bool:
    return os.environ.get("DEEPEVIDENCE_DEBUG", "").strip().lower() in ("1", "true", "yes", "on")


def _print_error(msg: str, *, debug_exc: Optional[Exception] = None) -> None:
    print(msg)
    if debug_exc is not None and _debug_enabled():
        # Avoid printing full request/response; only include minimal exception string.
        print(f"(debug) {type(debug_exc).__name__}: {debug_exc}", file=sys.stderr)


def _status_code_from_exc(exc: Exception) -> Optional[int]:
    for attr in ("status_code", "http_status"):
        v = getattr(exc, attr, None)
        if isinstance(v, int):
            return v
    resp = getattr(exc, "response", None)
    if resp is not None:
        v = getattr(resp, "status_code", None)
        if isinstance(v, int):
            return v
    return None


def _is_timeout_exc(exc: Exception) -> bool:
    name = type(exc).__name__.lower()
    if "timeout" in name:
        return True
    cause = getattr(exc, "__cause__", None)
    if cause is not None and "timeout" in type(cause).__name__.lower():
        return True
    return False


def _is_connection_exc(exc: Exception) -> bool:
    name = type(exc).__name__.lower()
    if "connection" in name:
        return True
    cause = getattr(exc, "__cause__", None)
    if cause is not None and "connection" in type(cause).__name__.lower():
        return True
    return False


def _handle_api_exception(exc: Exception) -> None:
    status = _status_code_from_exc(exc)
    if status == 401:
        _print_error("Authentication failed: please check DEEPEVIDENCE_API_KEY.", debug_exc=exc)
        sys.exit(1)
    if status == 429:
        _print_error("Rate limit exceeded or quota exhausted: please retry later or contact your administrator.", debug_exc=exc)
        sys.exit(1)
    if status is not None and status >= 500:
        _print_error("Service temporarily unavailable: please retry later.", debug_exc=exc)
        sys.exit(1)
    if _is_timeout_exc(exc):
        _print_error(DEFAULT_TEMP_UNAVAILABLE_MSG, debug_exc=exc)
        sys.exit(1)
    if _is_connection_exc(exc):
        _print_error(DEFAULT_TEMP_UNAVAILABLE_MSG, debug_exc=exc)
        sys.exit(1)
    _print_error(DEFAULT_TEMP_UNAVAILABLE_MSG, debug_exc=exc)
    sys.exit(1)


def get_client():
    api_key = os.environ.get("DEEPEVIDENCE_API_KEY")
    if not api_key:
        _print_error(
            "Missing configuration: DEEPEVIDENCE_API_KEY is not set.\n"
            "Please apply for an API key at: https://deepevid.medsci.cn/platform/api-keys\n"
            "Then set it with: export DEEPEVIDENCE_API_KEY='your-key-here'"
        )
        sys.exit(1)
    # Fixed public base URL from https://deepevid.medsci.cn/platform/docs.
    base_url = "https://deepevid.medsci.cn/api/v1"
    return OpenAI(api_key=api_key, base_url=base_url)


def _load_json_arg(value: Optional[str], label: str):
    if not value:
        return None
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as exc:
        _print_error(f"Invalid {label}: expected valid JSON. {exc}")
        sys.exit(1)
    if not isinstance(parsed, dict):
        _print_error(f"Invalid {label}: expected a JSON object.")
        sys.exit(1)
    return parsed


def _build_user_content(query, image_urls=None):
    image_urls = image_urls or []
    if not image_urls:
        return query
    content = []
    if query:
        content.append({"type": "text", "text": query})
    for url in image_urls:
        content.append({"type": "image_url", "image_url": url})
    return content


def chat(
    query,
    user=None,
    conversation_id=None,
    locale=None,
    display_label=None,
    contact_id=None,
    model="DeepEvidence-V1",
    store=None,
    stream=False,
    include_usage=False,
    project_id=None,
    entity_encryption_ids=None,
    chat_mode=None,
    case_info=None,
    image_urls=None,
    user_name=None,
    user_email=None,
    user_metadata=None,
):
    """Send a medical question to DeepEvidence and print the response."""
    client = get_client()

    kwargs = {
        "model": model,
        "messages": [{"role": "user", "content": _build_user_content(query, image_urls)}],
        "stream": stream,
    }
    if stream and include_usage:
        kwargs["stream_options"] = {"include_usage": True}

    # Do not auto-read/upload OS usernames. Only send an external user ID if explicitly provided.
    if user:
        if not user.startswith("skill_"):
            user = f"skill_{user}"
        kwargs["user"] = user

    metadata = {}
    if conversation_id:
        metadata["conversation_id"] = conversation_id
    if locale:
        metadata["locale"] = locale
    if project_id:
        metadata["project_id"] = project_id
    if entity_encryption_ids:
        metadata["entity_encryption_ids"] = entity_encryption_ids
    if chat_mode:
        metadata["chat_mode"] = chat_mode
    if case_info:
        metadata["case_info"] = case_info
    if user_name:
        metadata["user_name"] = user_name
    if user_email:
        metadata["user_email"] = user_email
    if user_metadata:
        metadata["user_metadata"] = user_metadata
    if display_label:
        metadata["display_label"] = display_label
    if contact_id:
        metadata["contact_id"] = contact_id
    extra_body = {}
    if store is not None:
        extra_body["store"] = store
    if metadata:
        extra_body["metadata"] = metadata
    if extra_body:
        kwargs["extra_body"] = extra_body

    try:
        response = client.chat.completions.create(**kwargs)
    except Exception as e:
        _handle_api_exception(e)

    if stream:
        for chunk in response:
            choices = getattr(chunk, "choices", None)
            if choices:
                delta = getattr(choices[0], "delta", None)
                content = getattr(delta, "content", None) if delta else None
                if content:
                    print(content, end="", flush=True)
            usage = getattr(chunk, "usage", None)
            if usage:
                print(f"\n[tokens: prompt={usage.prompt_tokens}, completion={usage.completion_tokens}, total={usage.total_tokens}]")
        print()
        return response

    if not response or not getattr(response, "choices", None) or not response.choices:
        _print_error(DEFAULT_TEMP_UNAVAILABLE_MSG)
        sys.exit(1)
    if not getattr(response.choices[0], "message", None) or not getattr(response.choices[0].message, "content", None):
        _print_error(DEFAULT_TEMP_UNAVAILABLE_MSG)
        sys.exit(1)

    # Print answer
    print(response.choices[0].message.content)

    # Print metadata if available
    resp_dict = response.model_dump() if hasattr(response, "model_dump") else {}
    conv_id = resp_dict.get("metadata", {}).get("conversation_id")
    if conv_id:
        print(f"\n--- conversation_id: {conv_id} ---")

    # Print usage
    if response.usage:
        print(f"[tokens: prompt={response.usage.prompt_tokens}, completion={response.usage.completion_tokens}, total={response.usage.total_tokens}]")

    return response


def main():
    parser = argparse.ArgumentParser(description="DeepEvidence Medical Q&A")
    parser.add_argument("query", help="Medical question to ask")
    parser.add_argument("--model", default="DeepEvidence-V1", help="Model ID or public alias. Default: DeepEvidence-V1")
    parser.add_argument("--user", default=None, help="External user ID for multi-tenant isolation (OPTIONAL). Not sent unless provided.")
    parser.add_argument("--conversation-id", help="Continue an existing conversation by ID")
    parser.add_argument("--locale", help="Language preference, e.g. 'en', 'zh-CN'")
    parser.add_argument("--project-id", help="Internal/authorized extension: project ID to load project context and attachments")
    parser.add_argument("--entity-encryption-id", action="append", dest="entity_encryption_ids", help="Internal/authorized extension: restrict retrieval to an entity_encryption_id. Repeat for multiple IDs.")
    parser.add_argument("--chat-mode", choices=["auto", "fast", "expert"], help="Internal/authorized extension: optional chat mode metadata. Current server may only read/log this value.")
    parser.add_argument("--case-info-json", help="Internal/authorized extension: JSON object for case workflows")
    parser.add_argument("--image-url", action="append", dest="image_urls", help="Image URL or data:image/... base64 URL. Repeat for multiple images.")
    parser.add_argument("--no-store", action="store_true", help="Internal/authorized extension: send store=false so the server does not persist user/assistant/source messages")
    parser.add_argument("--stream", action="store_true", help="Use streaming response output")
    parser.add_argument("--include-usage", action="store_true", help="When streaming, request usage chunks")
    parser.add_argument("--user-name", help="Optional external user name metadata. Avoid PII unless contractually required.")
    parser.add_argument("--user-email", help="Optional external user email metadata. Avoid unless necessary.")
    parser.add_argument("--user-metadata-json", help="Optional external user metadata JSON object")
    parser.add_argument("--display-label", help="Optional label for the user (non-PII, e.g. 'Clinic-A')")
    parser.add_argument("--contact-id", help="Optional stable identifier (non-PII, e.g. 'ID-123')")
    args = parser.parse_args()

    chat(
        args.query,
        user=args.user,
        conversation_id=args.conversation_id,
        locale=args.locale,
        display_label=args.display_label,
        contact_id=args.contact_id,
        model=args.model,
        store=False if args.no_store else None,
        stream=args.stream,
        include_usage=args.include_usage,
        project_id=args.project_id,
        entity_encryption_ids=args.entity_encryption_ids,
        chat_mode=args.chat_mode,
        case_info=_load_json_arg(args.case_info_json, "--case-info-json"),
        image_urls=args.image_urls,
        user_name=args.user_name,
        user_email=args.user_email,
        user_metadata=_load_json_arg(args.user_metadata_json, "--user-metadata-json"),
    )


if __name__ == "__main__":
    main()
