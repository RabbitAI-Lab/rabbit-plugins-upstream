## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to maintain a GitLab agent profile with monthly contribution charts and a JSON record of counted activity. It supports checking project coverage and contribution totals while keeping private project details out of the public proof file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The updater can automatically download and run additional software without clearly disclosing that behavior.

Mitigation: Require a reviewed, preinstalled converter and remove or disable the automatic npm fallback.

Risk: Contribution totals include private or internal activity and may be published in the profile output.

Mitigation: Confirm the project scope and profile repository, then review the anonymized private activity totals before publishing.

## Reference(s):

- [ClawHub release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, SVG, WebP]

**Output Format:** [Static SVG and WebP contribution charts, plus a JSON proof file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The proof file includes public counted records and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.118.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
