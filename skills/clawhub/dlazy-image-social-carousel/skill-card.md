## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social media teams use the skill to plan a carousel’s narrative and slide content, confirm the direction, and generate a cover before matching the remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local media may be sent to dLazy hosted APIs and media storage for processing.

Mitigation: Avoid sending sensitive content unless its use with the service is approved, and confirm which files are included before generation.

Risk: The benign scanner verdict is based on partial inspection, and the release evidence notes possible setup and interaction-flow differences.

Mitigation: Review the CLI setup and skill workflow before use, and try the process with non-sensitive content first.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown with structured slide plans and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Carousel direction and slide plan, followed by cover-first image-generation requests and result URLs.]

## Skill Version(s):

1.3.43 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
