# Data flow and retention

This is a Google Gemini cloud-analysis skill, not local-only video processing. Cloud authorization covers both video and prompts, including any explicitly selected prior context. Ask before sending confidential, customer, private, or local recordings unless the current request already explicitly authorizes Google Gemini processing. The CLI enforces an --allow-cloud acknowledgement before authentication or cloud requests. Agentic processing itself is always on.

## Destinations and authentication

- Google GenAI SDK sends selected video uploads, URLs, and prompts to Google's Gemini API (generativelanguage.googleapis.com). YouTube URLs are fetched by Google; non-YouTube public video downloads contact the supplied host through yt-dlp.
- uv resolves the pinned google-genai SDK and its dependencies from the configured Python package index. yt-dlp and ffmpeg are local executables, called without a shell.
- Authentication uses GEMINI_API_KEY or GOOGLE_API_KEY from a host-owned managed environment when configured. For existing installations, the script also reads those exact keys from ~/.openclaw/secrets/openclaw-runtime.json or apiKey/providers.gemini.apiKey in ~/.video-understand/config.json. It does not search unrelated files or write credentials. Never print or request credential values; use the host's secure setup path.
- There is no source-domain allowlist. HTTP(S) video URLs and normal query parameters are supported. URL userinfo and common credential-bearing query parameters are rejected; this is not an exhaustive secret detector. Do not enter a signed URL into the command first and rely on rejection to protect shell history. Use an authorized local file instead.

## Retention

- Interactions use store=False. This disables retrievable interaction history; it is not a promise of zero provider retention or training exclusion. Confirm the organization's Gemini account/data terms before sensitive processing.
- Temporary uploads are deleted after analysis. --reuse-file-cache deliberately retains uploads until explicit purge or provider expiry. --keep and --download-only deliberately retain downloaded files.
- Source URLs, raw local paths, and session names are not persisted in cache identity records. Records use hashed lookup keys; remote handle names remain only where needed for reuse or cleanup. Legacy sensitive identity fields are removed when a record is rewritten, not retroactively across unrelated caches.
- --save-history explicitly stores questions and model outputs locally. --continue-chat requires it. --session-key and upload reuse alone do not save transcript history. Local record writes are atomic mode 0600, newly created cache directories mode 0700, and output files mode 0600. These are access restrictions, not encryption.
- --purge-cache removes matching remote handles and the local record, not separately requested output files or retained downloads. Source/session identity must remain stable to locate the record. Review existing v2.0.1 caches with their original source/session and purge sensitive records; this upgrade does not claim to erase old logs or unrelated files.
- If remote deletion fails, the operation fails visibly and keeps minimal cleanup handles locally. Retry purge. Never claim sensitive data was deleted until the provider confirms deletion.
- Stderr suppresses sources and raw error bodies. Stdout and explicit output/history files contain requested video-derived content and must be delivered/stored only where authorized.

## Network authority

Downloading is an intentional local-tool capability, not an internet-facing fetch service. Only run the user's authorized video source. yt-dlp may follow redirects and fetch manifests, segments, and CDN resources. This script does not provide DNS-rebinding or private-network isolation. If used with untrusted requests, the host must enforce egress restrictions across the downloader process and any child processes; do not claim URL validation alone prevents SSRF. A security review may flag this broad network capability. Report that limitation rather than deleting video-source support to obtain a clean score.
