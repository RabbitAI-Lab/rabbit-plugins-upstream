## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab profile with monthly contribution charts and a JSON record of counted activity. It supports reviewing project coverage, contribution categories, and anonymized private activity totals before publishing the profile assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The profile updater can automatically download and run unpinned software with access to GitLab credentials.

Mitigation: Before enabling unattended updates, remove the automatic npm fallback and provision a reviewed converter; restrict GitLab access to intended projects and publishing access to the profile repository.

Risk: Private and internal activity contributes to public profile totals.

Mitigation: Review the anonymized private-activity aggregates before publication.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, SVG charts, WebP charts, JSON records]

**Output Format:** [Static SVG and WebP charts plus a JSON contribution record file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to the last 12 completed calendar months. Public counted records are listed individually; private and internal activity is summarized by month, kind, and category.]

## Skill Version(s):

1.124.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
