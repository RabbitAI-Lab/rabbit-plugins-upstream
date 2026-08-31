## Description:

Use before installing, trusting, or running any third-party OpenClaw skill, and when the user says "scan this skill", "is this skill safe", "vet/check this skill", "should I install this", "audit my skills", or "clawvet".

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and agent users use ClawVet to scan untrusted OpenClaw skills before installation, summarize the scanner's grade and findings, and decide whether to install, review, or block the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a third-party npm scanner through npx.

Mitigation: Use the default offline scan for untrusted local skills, and enable remote or semantic modes only when network access or an optional Anthropic API key is intended.

Risk: Untrusted skill text can contain prompt injection, hidden payloads, or credential-grabbing instructions.

Mitigation: Treat the reviewed skill as untrusted input and rely on the scanner's JSON grade, score, recommendation, and findings before deciding whether to install.

## Reference(s):

- [ClawVet on ClawHub](https://clawhub.ai/mohibshaikh/skills/clawvet)
- [Publisher profile](https://clawhub.ai/user/mohibshaikh)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and scanner verdict summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the scanner grade, risk score, recommendation, relevant findings, and install, review, or block call.]

## Skill Version(s):

0.11.2 (source: server release metadata; artifact frontmatter reports 0.11.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
