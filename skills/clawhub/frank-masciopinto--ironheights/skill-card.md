## Description:

Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Ironheights to scan skills locally before trusting or installing them, and to review changes after approval or assess repository threat models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan review is incomplete because some local references could not be resolved.

Mitigation: Review the unresolved references before relying on the scan when complete coverage matters.

Risk: A hostile skill may try to bypass an agent that runs the scan itself.

Mitigation: Run Ironheights directly or use another trusted process outside the agent.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights ClawHub release](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Concise scan summaries and user guidance, based on structured scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory findings; does not itself approve or install skills]

## Skill Version(s):

1.21.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
