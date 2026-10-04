## Description:

Guides users through OpenMAIC setup, interactive classroom generation, and product or SDK extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and educators use this skill to set up OpenMAIC locally or use its hosted service, generate interactive classrooms, and customize the product or build with its SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live Demo sends the configured access code to the hosted OpenMAIC service.

Mitigation: Use the hosted service only when intended; keep the code in local configuration rather than sharing it in chat.

Risk: Approved local teaching materials may be uploaded to the selected OpenMAIC server.

Mitigation: Confirm before reading and uploading files, and review their contents and destination first.

Risk: Cloning, installing dependencies, or starting Docker changes the local environment.

Mitigation: Review the commands and obtain confirmation before running them.

## Reference(s):

- [OpenMAIC on ClawHub](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC hosted service](https://open.maic.chat)
- [Live Demo guide](references/live-demo.md)
- [Classroom generation guide](references/generate-flow.md)
- [Provider configuration guide](references/provider-keys.md)
- [Extension guide](references/extend.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code, Classroom links]

**Output Format:** [Markdown with code blocks and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a generated classroom URL after a successful job.]

## Skill Version(s):

0.3.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
