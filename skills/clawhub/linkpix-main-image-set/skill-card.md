## Description:

LinkPix uses qhkit to generate ecommerce main-image and carousel image sets from a product image, optional marketing copy, and platform-specific options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to prepare product main images, carousel sets, and platform-adapted listing visuals from a reference product image. Agents use it to install or configure qhkit, estimate generation cost, confirm paid generation parameters, and return generated image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add or upgrade local Node and qhkit tooling.

Mitigation: Review installation commands and package sources before use, and run the skill in an environment where local tooling changes are acceptable.

Risk: Product images, marketing copy, and generation parameters are sent to the qhkit/LinkPix service.

Mitigation: Use only content the user is authorized to upload, and avoid sensitive product or campaign material unless the service is approved for that data.

Risk: API keys may be mishandled if pasted directly into chat.

Mitigation: Configure the qhkit token through a secure local secret mechanism or environment variable and review local credential storage before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-set)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix service](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command output summaries, estimated or actual credit usage, and generated image URLs.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
