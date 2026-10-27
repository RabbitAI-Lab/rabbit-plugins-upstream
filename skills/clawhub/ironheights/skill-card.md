## Description:

Security scanner for skills. Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to scan skill files for suspicious installers, shell commands, encoded payloads, and credential theft before trusting or installing them. It explains scan findings and leaves installation and update decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hostile skill may try to bypass an in-agent scan, and Ironheights is advisory.

Mitigation: Run Ironheights yourself or through another trusted process outside the agent, and review the skill before relying on the result.

Risk: The separate Ironheights CLI dependency is outside this artifact review.

Mitigation: Keep CLI installation and updates under user control, and use only the npm package or GitHub repository identified by the skill as official sources.

## Reference(s):

- [Ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)
- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report, October 2026](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights source repository (listed by the skill)](https://github.com/Frank-Masciopinto/ironheights)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown summary of scan findings, with shell commands when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scans run locally with no telemetry stated. The CLI checks for updates every six hours; this can be disabled with IRONHEIGHTS_NO_UPDATE=1.]

## Skill Version(s):

1.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
