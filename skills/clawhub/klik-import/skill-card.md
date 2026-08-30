## Description:

Import your agent's memory files and scheduled tasks into Klik.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyixu](https://clawhub.ai/user/chengyixu)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect agent memory files and durable scheduled tasks, review and clean the draft payload, and upload it to Klik with a one-time import code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow transfers agent memory and scheduled task content to Klik.

Mitigation: Install only when that transfer is intended, review the import summary before approval, and avoid importing private, proprietary, or regulated information unless storing it in Klik is acceptable.

Risk: Collected memory or task text may contain secrets or personal data.

Mitigation: Use the built-in secret redaction and optional email redaction, then review the cleaned draft and skipped-file summary before confirming upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chengyixu/skills/klik-import)
- [Agent Skills v1.0 specification](https://agentskills.io/specification)
- [Klik pre-launch information](https://pre.hiklik.ai/?utm_source=github&utm_medium=readme&utm_campaign=kickstarter_prelaunch&utm_content=klik_import_skill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON payload drafts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a temporary JSON payload for validation and upload; prompts the user for confirmation before submitting data.]

## Skill Version(s):

0.1.0 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
