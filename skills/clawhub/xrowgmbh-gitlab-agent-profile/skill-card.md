## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab agent profile with monthly contribution charts and a public proof file containing public records and anonymized private activity totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The legacy script’s automatic npm fallback can download and run unpinned software while the collector has access to credentials.

Mitigation: Use an approved, preinstalled renderer and avoid the legacy fallback.

Risk: Scheduled publication depends on a separately installed Node.js plugin.

Mitigation: Verify the plugin before enabling scheduled publication, then inspect outputs before pushing.

Risk: The private profile-reports.json file may contain information that should not be published.

Mitigation: Keep profile-reports.json private; publish only the public records and anonymized private monthly totals intended for the profile.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [SVG and WebP charts, JSON contribution records, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The public proof file includes public counted records and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.127.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
