## Description:

Analyzes pet food-bowl videos to estimate eating duration and speed, then provides slow-feeding suggestions when results fall below a safety threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-feeder applications can use the skill to review a pet's eating behavior from a bowl-area video, see estimated feeding times and speed, and receive a slow-feeding suggestion. It provides behavioral information and does not diagnose disease.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos and supplied URLs are sent to LifeEmergence services and may contain sensitive imagery or secrets.

Mitigation: Avoid private footage and URLs containing secrets; review the service destination and its data handling before submitting video.

Risk: The security review flags account and credential handling concerns, and the export-only option may still upload videos.

Mitigation: Wait for these controls to be corrected before using valuable credentials; confirm account creation, local token protection, and deletion controls, and do not rely on export-only behavior to prevent uploads.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding start and end times, estimated eating speed, threshold comparisons, intervention suggestions, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
