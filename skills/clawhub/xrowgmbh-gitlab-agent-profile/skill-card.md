## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

GitLab maintainers and agent operators use this skill to collect monthly contribution activity and publish a profile chart with public proof records and anonymized private totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The profile updater can automatically download and run third-party software with access to GitLab credentials.

Mitigation: Replace the automatic npm fallback with a preinstalled, pinned converter before enabling scheduled updates. Restrict GitLab access to intended projects, and confirm that publishing activity totals and automatically pushing profile assets are acceptable.

## Reference(s):

- [GitLab Agent Profile skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance]

**Output Format:** [Static SVG and WebP charts, plus a JSON proof file and Markdown operating instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The proof file includes public counted records and monthly totals for private or internal activity while omitting private project details.]

## Skill Version(s):

1.122.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
