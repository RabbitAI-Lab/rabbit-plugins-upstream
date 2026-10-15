## Description:

Helps create batches of product video ads for feed placements, brand campaigns, and social media marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and advertisers use this skill to generate multiple product video ads for feed placements, brand promotion, and social campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external npm package and service.

Mitigation: Review the qhkit package and version before installing or running it.

Risk: Service access requires an API token.

Mitigation: Provide the token only through the service's supported configuration or environment variable and avoid sharing it in messages.

Risk: Generating videos may consume paid credits and submitted tasks cannot be cancelled.

Mitigation: Check estimated credits and obtain user confirmation before submitting supported video tasks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-video-ad-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples and video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs and credit usage for generated videos.]

## Skill Version(s):

0.1.2 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
