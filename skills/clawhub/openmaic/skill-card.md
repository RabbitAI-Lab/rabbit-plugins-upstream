## Description:

Guides agents through OpenMAIC setup, interactive classroom generation, and product or SDK customization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and educators use this skill to set up or access OpenMAIC, generate interactive classrooms from prompts and approved materials, and extend its application or SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A stored OpenMAIC access code may be used for authenticated requests.

Mitigation: Keep access codes private and confirm the target service before connecting.

Risk: Approved classroom materials may be uploaded to the selected server.

Mitigation: Confirm the server URL and review files before approving uploads.

Risk: Local setup commands may install dependencies or change a checkout.

Mitigation: Run setup commands only in a checkout you trust.

## Reference(s):

- [OpenMAIC skill release](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Classroom generation guide](artifact/references/generate-flow.md)
- [Provider configuration guide](artifact/references/provider-keys.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide a classroom link after generation.]

## Skill Version(s):

0.3.11 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
