## Description:

Security scanner for skills. Use before installing any skill from ClawHub or GitHub: flags malware, pipe-to-shell, encoded payloads, credential theft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use Ironheights to review skill files for suspicious content before trusting or installing a skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scans are advisory; the separately installed CLI must be trusted, and optional model review may send skill text to a server.

Mitigation: Verify the CLI independently, review scan findings before trusting a skill, and use model review only when remote sharing is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frank-masciopinto/skills/ironheights)
- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory scan summaries; results are not a guarantee that a skill is safe.]

## Skill Version(s):

1.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
