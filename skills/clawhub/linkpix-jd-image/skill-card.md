## Description:

Guides creation of JD.com product images, image sets, detail-page graphics, and promotional visuals through the Qinghu AI image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

JD.com merchants, advertising specialists, and brand teams use this skill to prepare product listings, image carousels, detail-page graphics, and campaign visuals from product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating unpinned Node/npm tools can change the software executed on the user's machine.

Mitigation: Prefer a pre-provisioned qhkit installation and review any package installation or update before running it.

Risk: Product images are uploaded to the qhkit service for processing.

Mitigation: Confirm that the user permits uploading the selected product images before submitting a generation task.

Risk: A qhkit API key may be stored locally during setup.

Mitigation: Prefer a managed secret store and avoid disclosing the key in chat or logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-jd-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Image URLs, Shell commands, Configuration guidance]

**Output Format:** [Markdown with image links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image links and actual credit usage are reported after completion.]

## Skill Version(s):

0.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
