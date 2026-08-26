## Description:

快速生成双11、黑五、圣诞节等营销活动海报与折扣营销图，适用于新品发布、促销活动及品牌宣传。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to guide agents in creating promotional poster prompts, qhkit image generation commands, and review steps for product launches, discounts, holiday campaigns, and brand marketing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys could be exposed if pasted into chat or stored insecurely.

Mitigation: Set QHKIT_TOKEN through a secure local environment variable or secret store, and avoid sharing the token in conversation.

Risk: Poster prompts or product images may be sent to the qhkit/LinkPix service.

Mitigation: Use the skill only with content approved for that service, and avoid sensitive product images or confidential campaign details unless the user accepts that transfer.

Risk: Generation requests may consume paid credits.

Mitigation: Estimate and confirm expected credit usage with the user before submitting any generation request.

Risk: Generated poster text, numbers, logos, or product details may be inaccurate.

Mitigation: Review generated images before use and regenerate or correct outputs when campaign copy or product details are wrong.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit image generation parameters, setup guidance, confirmation steps, and generated image delivery guidance.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
