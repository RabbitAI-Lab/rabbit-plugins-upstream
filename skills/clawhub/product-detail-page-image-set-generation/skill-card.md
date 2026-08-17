## Description:

Generates product-detail-page image sets from text prompts and optional reference images for e-commerce main images, detail pages, advertising key visuals, posters, social commerce assets, retouching, background replacement, and consistent-character visual content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, e-commerce operators, product photographers, brand teams, and live-commerce teams use this skill to generate product-detail image sets, product main images, advertising visuals, posters, and social media assets from text and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images may be uploaded to AI Hive when users provide them.

Mitigation: Use only images approved for AI Hive processing and avoid uploading private or sensitive files unless that transfer is intended.

Risk: Image-generation tasks can be billable, especially when batch size or routing choices change.

Mitigation: Review runtime pricing, routing mode, and batch size before submission, and retain task IDs to avoid accidental duplicate jobs.

Risk: Generated outputs are saved locally by default.

Mitigation: Choose an appropriate output directory, control file permissions where needed, and review generated assets before commercial reuse.

Risk: The artifact includes dormant generic chat, video, and account code outside the active image-generation skill path.

Mitigation: Use the documented image-generation commands and prefer a cleanup release that removes unused generic code for clearer scope.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/product-detail-page-image-set-generation)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files, guidance]

**Output Format:** [Markdown instructions with shell command examples, JSON task responses, and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI Hive API credentials; optional reference images may be uploaded; generated images are saved locally unless download is disabled.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
