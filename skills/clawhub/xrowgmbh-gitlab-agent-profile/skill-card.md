## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab agent profile with recent contribution statistics, chart assets, and public proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-conversion fallback may download and run an unpinned npm package.

Mitigation: Prefer an already installed ImageMagick converter, or review and pin the fallback package before allowing it to run.

Risk: The security scan is incomplete because referenced local paths were not found and the declared tool scope is missing.

Mitigation: Review the missing paths and required tools, and check GitLab credential handling before installing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Static SVG and WebP charts plus JSON proof records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The proof records include public counted activity and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.149.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
