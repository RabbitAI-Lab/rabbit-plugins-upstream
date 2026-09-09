## Description:

Use before installing, enabling, or running any third-party OpenClaw skill, and when the user says "install this skill", "is this skill safe", "scan/vet/check this skill", or "should I trust this".

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to scan third-party OpenClaw skills with ClawVet before installation, enablement, or execution, then act on the scanner's recommendation and severity findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the external ClawVet npm CLI against skill files.

Mitigation: Install only when comfortable with that CLI execution path and when node and npx are available in the environment.

Risk: A safety scan result could be mistaken for consent to install or enable a skill.

Mitigation: Use automatic installation only when the user explicitly asked to install or enable the skill; otherwise treat the result as advisory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet-guard)
- [ClawVet repository](https://github.com/MohibShaikh/clawvet)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and scanner-result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference JSON fields emitted by the ClawVet CLI, including recommendation and severity findings.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
