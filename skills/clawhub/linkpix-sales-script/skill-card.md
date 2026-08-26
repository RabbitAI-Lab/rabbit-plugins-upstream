## Description:

Generates ecommerce sales copy and video scripts from product images, selling points, or reference short-video links using LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and marketing teams use this skill to generate livestream, product-promotion, review, seeding, and story-style ecommerce scripts, or to reverse-engineer script ideas from reference viral videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the skill asks users to provide an API key and saves that credential for CLI use.

Mitigation: Do not paste API keys into chat; configure the token locally with qhkit or QHKIT_TOKEN, and review any credit-consuming task before approval.

Risk: The skill sends product images, reference links, and prompts to the LinkPix/qhkit provider.

Mitigation: Use only product assets and prompts that are appropriate to share with that third-party service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API Key Guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with generated script text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include complete ecommerce script text, status guidance, or CLI error messages.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
