## Description:

Generates ecommerce product detail-page image sets from product reference images, combining selling points, scenes, specifications, and marketing copy through the LinkPix qhkit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to turn product images into ordered detail-page image sets for listings, refreshes, long-form product pages, selling-point images, and A+ page-style content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images are uploaded to the Qinghu service for generation.

Mitigation: Use only images the user is permitted to upload and avoid submitting confidential or restricted product material unless the user approves that handling.

Risk: The workflow stores or uses a qhkit API key.

Mitigation: Keep the token out of public logs and files, prefer environment-based configuration where practical, and only request the key when qhkit reports that configuration is required.

Risk: Generation consumes service credits.

Mitigation: Run the estimate command with the same parameters, present the expected credit cost and key inputs, and wait for explicit user approval before running generation.

Risk: The skill may install Node/qhkit tooling before use.

Mitigation: Install qhkit from the declared npm package and follow the documented checksum step before unpacking downloaded Node binaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-detail-page)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Image URLs]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters; completed generation returns ordered image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, selected product images, an API key or QHKIT_TOKEN, and explicit user approval before credit-consuming generation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
