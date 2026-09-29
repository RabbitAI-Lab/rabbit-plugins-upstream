## Description:

Guides agents in generating and editing images with GPT Image 2.5 Flare through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to create images from prompts or edit images using reference inputs, with adjustable aspect ratio and quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected input files are sent to the third-party dLazy cloud service, where generated files are hosted.

Mitigation: Avoid submitting sensitive prompts or files; review the service's handling of uploaded and hosted content before use.

Risk: Logging in can store a dLazy API key locally.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if it is exposed.

Risk: Installing the third-party CLI globally persists executable software on the machine.

Mitigation: Review the pinned package or its linked source before installing; use the documented npx option if a persistent global install is not wanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI source (linked in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON with hosted image URLs and can save generated images locally.]

## Skill Version(s):

1.2.11 (source: ClawHub release evidence; artifact frontmatter and CLI install specify 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
