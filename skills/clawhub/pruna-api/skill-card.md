## Description:

Use before Pruna or Replicate HTTP calls for credentials, uploads, polling, downloads, parallel batches, and agent safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to prepare safe Pruna and Replicate API workflows, including credential checks, media uploads, prediction polling, output downloads, and parallel batch execution before paid calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports paid external API workflows that can incur cost when prediction or upload commands are run.

Mitigation: Confirm required API keys and user intent before paid POST requests, and resolve cost-sensitive media, resolution, duration, and approval-gate choices before execution.

Risk: Local media, scripts, portraits, or voices may be uploaded to Pruna or Replicate services.

Mitigation: Get explicit user acknowledgement before first upload or prediction, confirm rights and consent for likenesses or voices, and explain that content leaves the local environment.

Risk: API credentials could be exposed if copied into prompts, logs, manifests, or subagent instructions.

Mitigation: Read credentials only from environment variables or gitignored local configuration, never print full keys, and avoid distributing secrets to parallel workers unless isolated secret injection is documented.

Risk: Download commands can overwrite local files.

Mitigation: Confirm output paths before writing downloaded results and avoid clobbering unrelated files.

Risk: Installer commands may fetch executable skill packages with npx.

Mitigation: Consider pinning or otherwise verifying the npx skills installer before running installation commands.

## Reference(s):

- [ClawHub pruna-api release page](https://clawhub.ai/pruna-ai/skills/pruna-api)
- [API credentials](references/api-credentials.md)
- [Agent safety](references/agent-safety.md)
- [Pruna P-API shared reference](references/pruna-api.md)
- [Replicate API](references/replicate-api.md)
- [Pruna models index](references/pruna-models.md)
- [Pruna Developer Portal](https://docs.api.pruna.ai/)
- [Pruna API Quickstart](https://docs.api.pruna.ai/guides/quickstart)
- [Pruna Available Models](https://docs.api.pruna.ai/guides/models)
- [Replicate API Tokens](https://replicate.com/account/api-tokens)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include credential setup, upload and polling steps, download commands, and safety checks before paid external API calls.]

## Skill Version(s):

1.0.13 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
