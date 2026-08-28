## Description:

Use before any Pruna or Replicate HTTP call for credentials, upload, polling, download, parallel batches, and agent safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare Pruna and Replicate API calls, including credential setup, file upload, prediction polling, output download, and safety checks before paid or external-processing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media, scripts, narration text, and related inputs may be sent to Pruna or Replicate for remote processing.

Mitigation: Require explicit user acknowledgment before the first upload or paid prediction, and disclose that content leaves the local environment.

Risk: Portraits, voices, third-party likenesses, or identity replacement workflows can involve consent-sensitive material.

Mitigation: Confirm the user has permission to use any likeness, voice, portrait, or identity material before making external API calls.

Risk: API credentials could be exposed if copied into prompts, logs, manifests, committed files, or subagent instructions.

Mitigation: Read PRUNA_API_KEY and REPLICATE_API_TOKEN only from host environment variables or local uncommitted environment files, and never include full keys in generated content.

Risk: Downloaded outputs can overwrite local files.

Mitigation: Confirm output paths before writing downloaded files and avoid clobbering unrelated workspace paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api)
- [Pruna developer portal](https://docs.api.pruna.ai/)
- [Pruna quickstart](https://docs.api.pruna.ai/guides/quickstart)
- [Pruna models](https://docs.api.pruna.ai/guides/models)
- [Pruna dashboard](https://dashboard.pruna.ai/)
- [Replicate API tokens](https://replicate.com/account/api-tokens)
- [API credentials](references/api-credentials.md)
- [Agent safety](references/agent-safety.md)
- [Pruna P-API](references/pruna-api.md)
- [Replicate API](references/replicate-api.md)
- [Pruna models index](references/pruna-models.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell command examples and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request patterns, credential checks, upload and polling steps, download guidance, and safety reminders.]

## Skill Version(s):

1.0.10 (source: server release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
