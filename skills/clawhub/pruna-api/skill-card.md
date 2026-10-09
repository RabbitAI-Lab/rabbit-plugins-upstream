## Description:

Guides agents through Pruna and Replicate API credentials, uploads, prediction polling, downloads, parallel batches, and safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to prepare and run Pruna or Replicate media API workflows, including credential setup, file transfer, prediction tracking, and safe handling of paid calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User media may be uploaded to Pruna or Replicate for remote processing.

Mitigation: Confirm consent and the destination before uploading sensitive or third-party media.

Risk: API credentials could be exposed through chat, files, or logs.

Mitigation: Keep keys in environment variables and do not include them in chat, committed files, or logs.

Risk: Unpinned installation commands may fetch changing dependencies in privileged environments.

Mitigation: Prefer a pinned or preinstalled skills tool over running unpinned npx commands.

## Reference(s):

- [Pruna API skill on ClawHub](https://clawhub.ai/pruna-ai/skills/pruna-api)
- [Pruna API quickstart](https://docs.api.pruna.ai/guides/quickstart)
- [Pruna models](https://docs.api.pruna.ai/guides/models)
- [Replicate API guidance](artifact/references/replicate-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advises on credential checks, uploads, asynchronous polling, and downloads; does not itself generate media.]

## Skill Version(s):

1.0.14 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
