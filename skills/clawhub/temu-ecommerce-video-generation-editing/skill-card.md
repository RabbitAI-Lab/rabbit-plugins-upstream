## Description:

Create and edit Temu product catalog videos, factory demonstrations, assembly guides, variant clips and multi-market adaptations using Seedance generation and editing through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, content operators, and developers use this skill to generate and edit traceable Temu ecommerce videos from approved product records, SKU variants, factory footage, and market localization requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and can upload selected product images, videos, or audio to AI Hive for generation.

Mitigation: Use the documented commands, provide only media approved for third-party processing, and avoid confidential media unless that processing is acceptable.

Risk: Batch video generation can incur live service costs.

Mitigation: Confirm one SKU, check current routing and cost information, and manually approve the master video before scaling a batch.

Risk: Generated ecommerce videos may introduce unsupported product claims, incorrect variants, or inaccurate package contents.

Mitigation: Tie each output to the product master, SKU, market, and shot recipe; reject outputs that add unapproved deals, reviews, warranties, certifications, or performance claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/temu-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The packaged helper can upload selected media to AI Hive, poll generation tasks, and download resulting media files when invoked by the user.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
