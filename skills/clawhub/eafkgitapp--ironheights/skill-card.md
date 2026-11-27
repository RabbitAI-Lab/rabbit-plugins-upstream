## Description:

Ironheights, the immune system for AI agents, protects any AI bot that installs it (OpenClaw, Claude, Grok Bot, Codex, Cursor). Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft; also drift after approval and threat-model checks on every PR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eafkgitapp](https://clawhub.ai/user/eafkgitapp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use Ironheights to scan agent skills before installation and review changes to trusted skills or repository threat models. It provides advisory security checks to help identify suspicious content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial scan could not match some path-like references to bundled files, so those references were not covered by the review.

Mitigation: Review the referenced files separately and scan a complete copy of the skill before relying on the result.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report (October 2026)](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights on ClawHub](https://clawhub.ai/eafkgitapp/skills/ironheights)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown guidance and JSON scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
