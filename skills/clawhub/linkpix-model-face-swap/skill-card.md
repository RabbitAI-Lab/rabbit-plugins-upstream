## Description:

LinkPix helps agents replace ecommerce product-image or video models while preserving clothing, pose, composition, and lighting for localized product presentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, content teams, and agent users can use this skill to guide LinkPix/qhkit workflows for replacing models in product images or videos for localized storefront presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can support replacement of a person’s face, body, or video appearance without authorization.

Mitigation: Confirm the user has permission to use the likeness before processing media, and refuse unauthorized face or person replacement requests.

Risk: Generation jobs can upload local media and consume provider credits.

Mitigation: Use supported estimate actions before generation, summarize the key parameters and expected credit use, and wait for explicit user approval before submitting jobs.

Risk: Generated ecommerce images or videos may change product details, text, logos, or structure.

Mitigation: After generation, have the user review important commercial details before publishing the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit commands that upload local media, estimate credit use, submit generation jobs, poll status, and return generated media URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
