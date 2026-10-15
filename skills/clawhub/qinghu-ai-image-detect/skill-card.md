## Description:

Helps an agent assess whether an image is AI-generated using Qinghu's image-detection service and report its confidence score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and reviewers use this skill to check an image for signs of AI generation and understand the returned confidence score before deciding how to handle it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or image URLs are sent to Qinghu for analysis.

Mitigation: Only submit images the user is authorized and comfortable sharing with Qinghu.

Risk: Detection calls consume Qinghu credits.

Mitigation: Check the current estimate and obtain user consent before paid calls.

Risk: Setup can install or upgrade local tooling, alter shell startup files, and store an access token.

Mitigation: Review setup before running it, prefer an isolated or managed installation, avoid persistent shell changes unless intended, and protect the token.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ai-image-detect)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports an AI-generation confidence score from 0 to 1 and any credits charged; results depend on the external service.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
