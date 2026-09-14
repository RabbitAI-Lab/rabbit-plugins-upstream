## Description:

Use before any Pruna or Replicate HTTP call - credentials, upload/poll/download, parallel batches, and agent safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to prepare authenticated Pruna and Replicate API calls, upload and poll remote jobs, download generated media, and apply credential, privacy, and safety checks before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pruna or Replicate API calls may upload local media, portraits, voices, scripts, or copyrighted material to remote services for processing.

Mitigation: Obtain explicit user acknowledgment before the first upload or prediction, confirm consent for likenesses and voices, and tell the user that content leaves the local environment.

Risk: Documented commands may expose API credentials or send PRUNA_API_KEY to an untrusted delivery URL or redirect.

Mitigation: Read keys only from the host environment, never place keys in prompts, logs, manifests, or subagent task text, and validate Pruna download URLs and redirects before attaching the API key.

Risk: Install commands and paid POST calls can run mutable external code or incur cost without sufficient review.

Mitigation: Pin and verify installer and skill source where possible, avoid auto-confirmed installs, and confirm required credentials and user intent before paid POST requests.

Risk: Download commands can overwrite local files.

Mitigation: Confirm output paths before writing and avoid clobbering unrelated files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api)
- [Pruna P-API shared reference](references/pruna-api.md)
- [API credentials](references/api-credentials.md)
- [Agent safety](references/agent-safety.md)
- [Replicate API](references/replicate-api.md)
- [Pruna models index](references/pruna-models.md)
- [Pruna developer portal](https://docs.api.pruna.ai/)
- [Pruna quickstart](https://docs.api.pruna.ai/guides/quickstart)
- [Pruna available models](https://docs.api.pruna.ai/guides/models)
- [Pruna dashboard](https://dashboard.pruna.ai/)
- [Replicate API tokens](https://replicate.com/account/api-tokens)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell command examples and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may reference API keys, uploads, polling, downloads, and paid remote media generation flows; no generated media is produced by this helper skill itself.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
