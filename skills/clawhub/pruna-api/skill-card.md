## Description:

Guides agents before Pruna or Replicate HTTP calls, covering credentials, uploads, polling, downloads, parallel batches, and agent safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare Pruna or Replicate HTTP generation workflows, including credential setup, uploads, polling, downloads, and parallel batches. It also prompts safety checks before paid calls or media uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may leave the local environment for Pruna or Replicate cloud processing.

Mitigation: Get explicit user acknowledgement before the first upload or paid prediction and disclose remote processing.

Risk: API keys may be exposed if copied into prompts, logs, manifests, or subagent task text.

Mitigation: Read PRUNA_API_KEY and REPLICATE_API_TOKEN from environment variables only, and never print or commit full keys.

Risk: Paid generation calls and downloads can incur cost or overwrite local files.

Mitigation: Confirm required credentials, paid calls, unresolved media choices, and output paths before POST requests or local writes.

Risk: Floating install commands can install a changed package version.

Mitigation: Prefer pinned or verified skill install references over floating npx commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api)
- [Pruna P-API reference](references/pruna-api.md)
- [API credentials](references/api-credentials.md)
- [Agent safety](references/agent-safety.md)
- [Replicate API](references/replicate-api.md)
- [Pruna models](references/pruna-models.md)
- [Pruna Developer Portal](https://docs.api.pruna.ai/)
- [Pruna Quickstart](https://docs.api.pruna.ai/guides/quickstart)
- [Pruna model list](https://docs.api.pruna.ai/guides/models)
- [Replicate API tokens](https://replicate.com/account/api-tokens)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and HTTP API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential setup, upload, polling, download, batch execution, and safety guidance; it does not execute API calls by itself.]

## Skill Version(s):

1.0.11 (source: evidence.json release.version and SKILL.md frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
