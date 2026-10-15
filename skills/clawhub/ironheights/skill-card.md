## Description:

Scans OpenClaw skill folders locally with the ironheights CLI and explains findings before an agent trusts the skill.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users can scan new or updated skills for suspicious content and review findings before installing or using them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A scan with no findings may miss malicious behavior.

Mitigation: Treat results as advisory and review the skill before trusting or deploying it.

Risk: The scanner reads selected skill folders and stores local changed-scan state.

Mitigation: Scan only intended folders and account for local scan-state storage.

Risk: An unintended or untrusted scanner package could run on the user's machine.

Mitigation: Install only the intended ironheights package from its official npm or GitHub source.

## Reference(s):

- [ironheights website](https://www.ironheights.dev)
- [ClawHub skill listing](https://clawhub.ai/frank-masciopinto/skills/ironheights)
- [ClawHub Malicious Skills Report, October 2026](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain-language scan summary with findings and recommended next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verdicts, affected files and lines, and skipped files when a scan is incomplete.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
