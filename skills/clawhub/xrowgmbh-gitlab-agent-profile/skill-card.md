## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining a GitLab agent profile use this skill to collect monthly contribution activity and publish a chart and contribution record files to the profile repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bundled legacy script can download and run software while GitLab credentials are available.

Mitigation: Remove the runtime download fallback or provide a reviewed, version-pinned renderer before use.

Risk: Scheduled collection can include private or internal project activity in published aggregate totals.

Mitigation: Review the gitlab-agent plugin, confirm the GitLab group and permission scope, ensure aggregate publication is acceptable, and keep private snapshots out of commits.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, SVG and WebP charts]

**Output Format:** [SVG chart, WebP chart, and JSON contribution records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The JSON includes public counted records and anonymized monthly totals for private and internal activity.]

## Skill Version(s):

1.130.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
