## Description:

Use before installing, trusting, or running any third-party OpenClaw skill, and when the user says "scan this skill", "is this skill safe", "vet/check this skill", "should I install this", "audit my skills", or "clawvet".

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohibshaikh](https://clawhub.ai/user/mohibshaikh)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and OpenClaw users use ClawVet to scan third-party skills before installing, trusting, or running them, then act on the scanner's grade, findings, and recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: npx or npm may fetch and run the ClawVet package when the scan command is invoked.

Mitigation: Invoke ClawVet only when a skill-vetting workflow is intended, and review the returned JSON verdict before acting on it.

Risk: Semantic scans use ANTHROPIC_API_KEY when requested.

Mitigation: Use the static scan by default and provide the API key only when the semantic pass is explicitly requested.

Risk: The optional gate changes future OpenClaw skill-install policy.

Mitigation: Enable the gate deliberately with a global ClawVet install and remove or update that policy configuration when it is no longer wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and scanner-output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to report the scanner verdict, material findings, and an install, review, or block call.]

## Skill Version(s):

0.12.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
