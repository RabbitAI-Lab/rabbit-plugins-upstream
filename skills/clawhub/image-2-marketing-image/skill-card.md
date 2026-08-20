## Description:

Builds traceable GPT Image 2 campaign image workflows for master creative, channel derivatives, and localized marketing assets through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand, ecommerce, and campaign teams use this skill to create approved campaign master images, derive channel-specific assets, and localize visuals while preserving product, brand, and lineage constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or campaign images and prompt details are sent to AI Hive.

Mitigation: Use --preview to inspect generated prompts before uploading files or creating a task, and only submit images approved for the AI Hive workflow.

Risk: Saved API keys can expose AI Hive access if mishandled.

Mitigation: Protect the saved API key file or use an environment variable, and rotate the key if exposure is suspected.

Risk: Model-generated text, prices, claims, or legal details may be unsuitable for approved marketing materials.

Mitigation: Keep copy, prices, claims, legal details, and QR codes blank for approved post-production layout and review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/image-2-marketing-image)
- [AI Hive API endpoint used by the skill](https://ai-hive.iclip.cn/api)
- [AI Hive OpenAPI endpoint used by the script](https://ai-hive.iclip.cn/api/openapi/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, generated prompts, task status JSON, and downloaded image files when execution is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses one-image generation tasks and supports preview mode to inspect prompts before uploading files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
