## Description:

Guides users through OpenMAIC setup, interactive classroom generation, and product or SDK customization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Educators and developers use this skill to set up OpenMAIC, create interactive classrooms from instructions or PDFs, and customize the product or build with its SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live Demo requests may send classroom requirements or parsed PDF content to the hosted service.

Mitigation: Review content for sensitivity before submitting it to the hosted service; use local mode when appropriate.

Risk: Access codes and provider API keys could be exposed if pasted into chat or shared carelessly.

Mitigation: Keep credentials in local configuration files and avoid sharing their values in chat.

Risk: Local setup commands can install dependencies or start services.

Mitigation: Review setup commands and confirm installations or startup before running them.

## Reference(s):

- [OpenMAIC ClawHub release](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Live Demo guide](artifact/references/live-demo.md)
- [Classroom generation guide](artifact/references/generate-flow.md)
- [Provider configuration guide](artifact/references/provider-keys.md)
- [Extending OpenMAIC](artifact/references/extend.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with commands, configuration examples, and classroom links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guided setup and generation with confirmation before local file reads and state-changing actions.]

## Skill Version(s):

0.3.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
