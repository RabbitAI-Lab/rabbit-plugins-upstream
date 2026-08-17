## Description:

Create and edit SHEIN fashion product images, model try-on visuals, colorway sets, fabric details, outfit styling and campaign-ready bases. Use this skill for SHEIN商品图、服装主图、模特试穿、版型展示、面料细节、颜色SKU、穿搭图、尺码信息底图和跨境时尚电商；supports reference-guided AI Hive production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and creative production teams use this skill to generate and edit fashion product images, try-on visuals, colorway sets, fabric-detail images, outfit scenes, and campaign-ready base imagery for SHEIN-style listings. The skill supports reference-guided AI Hive image production while preserving garment structure, model proportions, color consistency, and merchant-approved product facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and can store it in ~/.ai-hive/config.json.

Mitigation: Treat the config file as a credential file, prefer environment variables or scoped keys where appropriate, and keep file permissions restricted.

Risk: Reference images supplied to generate or upload commands are sent to AI Hive.

Mitigation: Upload only intended product or reference images and avoid including sensitive, private, or unapproved media.

Risk: Generated ecommerce visuals can misrepresent garment fit, material, size, color, or brand claims if prompts are not reviewed.

Mitigation: Review outputs against merchant-approved garment details, avoid unprovided logos or claims, and check current SHEIN product and advertising requirements before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/shein-ecommerce-image-generation-editing)
- [AI Hive API Endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown with inline bash commands and CLI-generated JSON or downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, may upload user-selected reference images, submits image generation tasks, polls task status, and downloads generated image results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
