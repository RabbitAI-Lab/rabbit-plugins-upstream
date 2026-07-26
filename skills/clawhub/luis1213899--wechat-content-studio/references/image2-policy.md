# image2 Cover Policy

All WeChat article covers in this workflow use image2, model `gpt-image-2`, through the relay API:

```text
OPENAI_BASE_URL=https://luisclaw.cloud/v1
model=gpt-image-2
```

Rules:

- Do not call `https://api.openai.com/v1` for covers in this workflow.
- Do not downgrade to `gpt-image-1`, `gpt-image-1.5`, `dall-e-3`, or another image model.
- Read `OPENAI_API_KEY` from the environment only.
- Do not write keys into scripts, Markdown, logs, command history, or packaged files.
- Prefer proxy:

```text
HTTP_PROXY=http://127.0.0.1:7897
HTTPS_PROXY=http://127.0.0.1:7897
```

The cover workflow is confirmation-based:

1. Draft prompt with `image2-workflow.ps1 -Mode Draft`.
2. Show the prompt to the user.
3. Generate only after confirmation.
