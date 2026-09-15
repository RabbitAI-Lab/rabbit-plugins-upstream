## Description:

Mistral AI operates Mistral account workflows through the OOMOL mistral_ai connector and oo CLI for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to route Mistral AI account tasks through the OOMOL connector, including chat, agents, embeddings, OCR, audio transcription, files, libraries, batch jobs, and fine-tuning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer execution.

Mitigation: Review the installer path before installing and prefer a verified package, pinned release, checksum, signature check, or manual inspection instead of pipe-to-shell commands.

Risk: The skill can perform write and destructive Mistral account operations.

Mitigation: Use it only for intentional Mistral account work, inspect the live connector schema, and confirm exact payloads and targets before write or destructive actions.

Risk: The activation scope is broader than necessary for a connector with account-level actions.

Mitigation: Invoke the skill only when the user request clearly involves Mistral AI and choose the narrowest action needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mistral-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Mistral AI homepage](https://mistral.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Inspect the live connector schema before payload construction; confirm write and destructive actions before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
