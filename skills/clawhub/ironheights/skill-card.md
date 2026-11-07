## Description:

Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Ironheights to review skills before installation, check for changes after approval, and compare repository contents with a threat model. It provides advisory findings so users can decide whether to trust a skill and retain control of installation and updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The separately installed npm CLI implementation was outside this artifact review.

Mitigation: Review and obtain the CLI from its official sources before relying on its results.

Risk: Optional model review may send skill text to a server.

Mitigation: Keep model review off unless the user explicitly chooses to send the text.

Risk: The CLI periodically checks for new versions over the network.

Mitigation: Set IRONHEIGHTS_NO_UPDATE=1 to disable periodic version checks.

Risk: Clean scan results do not guarantee that a skill is safe, and a hostile skill may try to bypass an in-agent check.

Mitigation: Have the user or another trusted process run the review outside the skill being checked.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights ClawHub release page](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Plain text or Markdown with CLI commands and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory results for the selected skill, repository, or installed-skill state.]

## Skill Version(s):

1.19.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
