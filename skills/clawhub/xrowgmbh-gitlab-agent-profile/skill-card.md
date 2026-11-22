## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab account owners use this skill to maintain monthly contribution charts and proof records for a profile repository, combining public activity with anonymized private totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A script can download and run an unpinned npm package as a fallback, creating supply-chain risk; the scan is partial.

Mitigation: Avoid installation unless needed; ensure the legacy script cannot run, and review renderer dependencies before installing them through a controlled process. The scan evidence is incomplete because five referenced paths were missing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [SVG charts, WebP charts, JSON records, Shell commands]

**Output Format:** [SVG, WebP, and JSON files with command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers completed calendar months; private activity is published only as anonymized monthly totals.]

## Skill Version(s):

1.151.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
