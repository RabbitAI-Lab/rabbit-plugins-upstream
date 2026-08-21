## Description:

使用 Nano Banana 2 把广告简报变成可测试的广告图片，明确受众、单一主张、视觉证据、品牌资产、CTA 安全区与禁用表述。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creative operators, and agents use this skill to turn an advertising brief and approved product or brand references into image-generation prompts, shell commands, and ad creative candidates for review and testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to AI Hive during generation.

Mitigation: Use non-sensitive, approved brand and product assets before running the skill.

Risk: Generated outputs may contain ad claims, prices, or visual implications that are not approved for publication.

Mitigation: Have the投放 or brand review team manually verify copy, product facts, prices, disclaimers, and compliance before publishing.

Risk: The helper uses an API key and stores generated files locally by default.

Mitigation: Protect the API key like any other credential and store generated files in an approved local location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ad-image)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline bash commands and local image-generation outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are saved locally by the helper script; reference images and prompts are sent to AI Hive.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
