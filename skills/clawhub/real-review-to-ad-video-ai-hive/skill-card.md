## Description:

This skill helps brands, ecommerce operators, and ad teams turn authorized buyer reviews and product materials into review evidence groups, ad angles, subtitle cards, scene prompts, video variants, delivery records, and runnable AI-HIVE generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, marketing, and ad-production teams use this skill to transform traceable buyer reviews, authorized media, product facts, channel requirements, and audience goals into a production-ready Chinese workflow. It can also guide AI-HIVE API use for model lookup, media upload, pricing snapshot review, routed image or video generation, polling, download, and deterministic video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload review, product, image, video, or audio materials to AI-HIVE and use them for generated ad assets.

Mitigation: Use only authorized reviews and media, review media rights before uploading, remove private buyer details when needed, and keep unsupported product claims marked for verification.

Risk: Image or video generation can incur cost and depends on current model routing, price, and availability.

Mitigation: Confirm the prompt, model, routing mode, pricing snapshot, and budget before submitting generation tasks; use small samples before batch generation.

Risk: AI-HIVE API keys may be supplied through environment variables, command-line arguments, or a local config file.

Mitigation: Prefer environment variables when persistent local storage is not desired, avoid logging or committing keys, and keep any local config file permission-restricted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/real-review-to-ad-video-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local blueprint JSON, AI-HIVE task records, downloaded media paths, and ffmpeg-derived video files when the user runs the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
