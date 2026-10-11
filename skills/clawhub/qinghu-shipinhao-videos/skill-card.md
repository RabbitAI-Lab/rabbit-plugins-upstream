## Description:

Retrieves a WeChat Channels account's published video list with cursor-based pagination through Qinghu's data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to retrieve a WeChat Channels account's published videos, page through results, and review competitor posting activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency setup may install Node.js or npm packages, change PATH, or configure a qhkit token in the user's environment.

Mitigation: Review the skill before installation; perform dependency and token setup manually or in a disposable environment.

Risk: Video-list queries consume paid Qinghu credits.

Mitigation: Check the current estimate and obtain user consent before making paid calls; report actual credits used.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-videos)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary; tabular file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports cursor pagination; paid queries require prior user consent.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
