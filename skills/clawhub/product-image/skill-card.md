## Description:

产品图生成 helps agents plan and run Nano Banana 2 product-image generations using product-invariance notes and a five-shot commercial lens matrix for catalog, hero, macro, scale, and packaging images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, merchants, designers, and developers use this skill to generate commercially oriented product images from product descriptions and optional reference images while preserving visible product features across multiple shot types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for generation.

Mitigation: Use only product materials that are approved for sharing with AI Hive before running generation.

Risk: The skill stores or reads an AI Hive API key locally.

Mitigation: Store the API key with restricted file permissions or provide it through AI_HIVE_API_KEY, and rotate it if it may have been exposed.

Risk: --param values are forwarded directly to the provider API.

Mitigation: Review parameter names and values before generation to avoid unintended provider settings.

Risk: Generated product images may misrepresent physical details, included accessories, or product claims.

Mitigation: Compare outputs against approved source materials and require brand or merchant confirmation before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash command examples and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are downloaded to ~/Downloads/AiHive by default unless --no-download is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
