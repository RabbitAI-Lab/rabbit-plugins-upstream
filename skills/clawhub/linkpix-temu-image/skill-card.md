## Description:

Helps Temu and managed-commerce sellers use Qinghu AI through qhkit to generate product image sets, detail images, white-background images, multi-SKU layouts, and promotional graphics tailored to Temu merchandising.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce operators and agents use this skill to prepare Temu-ready product visuals from supplied product images and campaign copy. It guides model option lookup, cost estimation, image generation, task polling, and result delivery through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade mutable third-party command-line packages.

Mitigation: Use pinned and reviewed local dependencies where possible instead of global @latest installs.

Risk: The skill handles a Qinghu API credential during setup.

Mitigation: Configure the API key through a private secret mechanism and avoid pasting credentials into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-temu-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage after user-approved qhkit generation tasks.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
