## Description:

Generates ecommerce ad copy, promotional image prompts and LinkPix/qhkit image assets, with an alternate workflow for turning commerce videos into social post text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to draft ecommerce ad copy, generate channel-specific ad images, and repurpose commerce videos into social commerce text posts using LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broad installation and upgrade authority, including instructions to install or upgrade qhkit and Node tooling.

Mitigation: Preinstall and review a pinned qhkit version before use, and avoid letting the agent run arbitrary upgrade commands from tool messages.

Risk: The skill requires configuring a qhkit token and may call external LinkPix/qhkit services.

Mitigation: Use a dedicated token with appropriate scope, avoid sharing secrets in prompts, and confirm that external service use is acceptable for the content being processed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON CLI parameters, ad copy, image prompts, generated asset links, and credit usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external LinkPix/qhkit services and may require qhkit installation plus a configured token before image or video-derived content can be generated.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
