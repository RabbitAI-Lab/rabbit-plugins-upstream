## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use the skill to update monthly contribution charts and publish supporting contribution records for an agent profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image-conversion fallback can fetch and run an unpinned npm package. The security scan was partial, and the skill does not declare tool scope; this concern is not evidence of malicious intent.

Mitigation: Review or remove the npm fallback before installation, and understand and limit the credentials and permissions available when the skill runs.

## Reference(s):


## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [SVG and WebP charts, JSON contribution records, and Markdown operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes monthly contribution totals and anonymized private or internal activity summaries.]

## Skill Version(s):

1.134.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
