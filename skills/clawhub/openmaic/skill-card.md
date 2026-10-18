## Description:

Guides users through OpenMAIC classroom generation, local or hosted setup, and customization with the OpenMAIC SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to set up OpenMAIC, generate interactive classrooms from prompts and optional documents, or extend the product and its SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a repository, installing dependencies, or starting a local server changes the user's environment.

Mitigation: Review the proposed actions and confirm each state-changing step before execution.

Risk: Live Demo access codes and selected local documents may be sent to the hosted OpenMAIC service.

Mitigation: Keep access codes out of chat, confirm document reads and uploads, and avoid sensitive materials unless hosted processing is acceptable.

## Reference(s):

- [OpenMAIC skill listing](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [OpenMAIC project repository (installation reference)](https://github.com/THU-MAIC/OpenMAIC.git)
- [Generation workflow](references/generate-flow.md)
- [Provider configuration](references/provider-keys.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a generated classroom link after user-approved generation.]

## Skill Version(s):

0.3.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
