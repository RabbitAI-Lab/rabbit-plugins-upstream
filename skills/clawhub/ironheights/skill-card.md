## Description:

Ironheights protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and people managing AI agent skills use this advisory workflow to scan skills before installation, review changes after approval, and check repository threat models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review covers the skill instructions, not the separately installed Ironheights CLI.

Mitigation: Verify the npm dependency before running the CLI.

Risk: Optional model reviews may send skill text to a server.

Mitigation: Keep model review off unless the user explicitly requests it.

Risk: Ironheights periodically checks for new versions over the network.

Mitigation: Set IRONHEIGHTS_NO_UPDATE=1 to disable version checks.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report, October 2026](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with scan summaries and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory findings; installation, approval, and updates remain user-controlled.]

## Skill Version(s):

1.11.0 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
