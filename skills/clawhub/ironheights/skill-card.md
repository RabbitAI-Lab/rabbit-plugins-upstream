## Description:

Protects any AI bot's skills (OpenClaw, Claude, Grok Bot, Codex, Cursor) by scanning before installation for malware, pipe-to-shell commands, encoded payloads, and credential theft, with OWASP and OpenCRE tags on findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users reviewing agent skills can run Ironheights before trusting or installing a skill, then use its findings to decide what to inspect. The scan is advisory and does not guarantee a skill is safe.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An adversarial skill may evade an agent-run review or try to influence its result.

Mitigation: Have the user or a trusted process outside the agent run Ironheights, and treat the result as advisory before enabling the skill.

Risk: Model review can send skill text to a server, and a clean scan does not guarantee safety.

Mitigation: Use the local scan when skill text should stay local, review the skill independently, and do not treat a clean verdict as proof of safety.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/frank-masciopinto/skills/ironheights)
- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Plain-language scan findings with rule IDs, file paths, line numbers, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results; the skill does not install or modify scanned skills.]

## Skill Version(s):

1.6.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
