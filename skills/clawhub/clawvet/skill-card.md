## Description:

Clawvet guides an agent to scan untrusted OpenClaw skills with ClawVet before installing, trusting, running, or auditing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to vet third-party OpenClaw skills before installation or execution, using scanner grades and findings to decide whether to install, review, or block a skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill delegates scanning to the external clawvet npm tool via npx.

Mitigation: Use it for skill review workflows and enable remote or semantic scanning only when the related network or API use is acceptable.

Risk: Semantic scanning may require ANTHROPIC_API_KEY.

Mitigation: Run the default static offline scan unless the user explicitly asks for the semantic pass and approves the required credential use.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/mohibshaikh/skills/clawvet)
- [ClawHub publisher profile](https://clawhub.ai/user/mohibshaikh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with scanner verdicts, findings, recommendations, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scanner JSON fields such as riskScore, riskGrade, recommendation, severity, and file or line locations.]

## Skill Version(s):

0.11.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
