## Description:

Guides users through OpenMAIC setup, interactive classroom generation, and customization of the product or its SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wyuc](https://clawhub.ai/user/wyuc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other OpenMAIC users can set up a local instance or connect to the Live Demo, generate interactive classrooms from prompts or PDFs, and get guidance on extending the app or SDK.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF-based generation may send sensitive document contents to the configured OpenMAIC endpoint without a clear warning.

Mitigation: Explain where the PDF contents will be sent and obtain consent before reading or uploading sensitive files.

Risk: A stored Live Demo access code can be exposed if the local OpenClaw configuration is shared or readable by others.

Mitigation: Protect ~/.openclaw/openclaw.json like a password and never paste the access code into chat.

## Reference(s):

- [OpenMAIC skill release](https://clawhub.ai/wyuc/skills/openmaic)
- [OpenMAIC Live Demo](https://open.maic.chat)
- [Classroom generation flow](artifact/references/generate-flow.md)
- [Live Demo setup](artifact/references/live-demo.md)
- [Extending OpenMAIC](artifact/references/extend.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with commands, code examples, and classroom links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a classroom URL after a generation job succeeds.]

## Skill Version(s):

0.3.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
