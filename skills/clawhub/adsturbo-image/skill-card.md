## Description:

AdsTurbo AI 图片创作 helps agents generate and edit images for ecommerce and marketing, including background removal, product images, campaign posters, watermark or object removal, and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or edit marketing and product imagery through AdsTurbo. Typical tasks include text-to-image generation, product shot sets, campaign posters, background removal, authorized object or watermark removal, and upscaling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media is sent to AdsTurbo and may be returned as public URLs.

Mitigation: Use only media approved for AdsTurbo processing, avoid sensitive private assets, and confirm the user understands that local files must be uploaded before image operations.

Risk: Watermark or object removal can be misused on images the user is not authorized to modify.

Mitigation: Use erase or watermark-removal workflows only when the user owns the image or has explicit permission to edit it.

Risk: The dependency specification uses a broad lower bound for requests.

Mitigation: Pin or review the requests package version in controlled deployments before installing the skill.

## Reference(s):

- [AI 图片创作 / Image](references/image.md)
- [素材上传 / Upload](references/upload.md)
- [任务状态 / Work Status](references/work.md)
- [AdsTurbo](https://www.adsturbo.ai)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-image)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, image URLs]

**Output Format:** [Markdown guidance with bash commands and returned JSON or public image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return public media URLs or workspace IDs for asynchronous AdsTurbo jobs.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
