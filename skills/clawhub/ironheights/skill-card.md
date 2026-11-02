## Description:

Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Ironheights to inspect skills before trusting or installing them, check approved skills for changes, and compare repository skills with a threat model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hostile skill may try to bypass a check running inside the same agent.

Mitigation: Run Ironheights from a trusted process outside the agent when reviewing a skill.

Risk: The separate npm CLI implementation was unavailable for this review.

Mitigation: Obtain the CLI only from the official npm package and project repository identified by the skill, and review that dependency separately.

Risk: Optional model review can send skill text to a server.

Mitigation: Keep model review disabled unless the user explicitly chooses to share the skill text.

## Reference(s):

- [ClawHub Malicious Skills Report, October 2026](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Project repository](https://github.com/Frank-Masciopinto/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Shell commands]

**Output Format:** [JSON scan results with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scans local skill files; requires the separate ironheights CLI and Node.js 20 or newer.]

## Skill Version(s):

1.18.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
