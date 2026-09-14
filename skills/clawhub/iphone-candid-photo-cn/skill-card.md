## Description:

用中文生成真实、带自然瑕疵感的 iPhone 随手拍风格照片提示词或结构化 JSON,并可在图像工具可用时引导直接生成图像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrestneo](https://clawhub.ai/user/forrestneo)

### License/Terms of Use:

MIT

## Use Case:

创作者、设计师和使用中文图像生成工具的开发者可用它把简短场景描述转为 iPhone 随手拍风格的中文提示词、审计用 JSON 提示词或参考图引导说明。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill strongly defaults to Simplified Chinese and an iPhone candid-photo aesthetic, which may be unwanted for English, studio, DSLR, cinematic, or non-phone photography requests.

Mitigation: Ask explicitly for English output or a non-phone, studio, DSLR, or cinematic look when that style is required.

Risk: Generated prompts may overfit to phone-shot realism cues such as imperfections, casual framing, and reference-image preservation.

Mitigation: Review prompts before image generation and adjust subject, identity, style, and exclusion terms when the request needs different visual constraints.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/forrestneo/iphone-candid-photo-cn)
- [ClawHub skill page](https://clawhub.ai/forrestneo/skills/iphone-candid-photo-cn)
- [Structured prompt schema](references/schema.md)
- [Original inspiration notice](NOTICE.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Simplified Chinese prompt text or structured JSON prompt object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to Simplified Chinese, preserves camera and product terms in English, and steers outputs toward iPhone-style candid photography unless the user asks otherwise.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
