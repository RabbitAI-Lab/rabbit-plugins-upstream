## Description:

Turns product links or supplied product-page facts into TikTok-first ecommerce content workflows with fact tables, English hooks, UGC scripts, AI-HIVE image and video generation commands, task records, and 9:16 video revision steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, cross-border marketing teams, and TikTok Shop operators use this skill to convert authorized product information and media into reviewable creative plans, scripts, AI-HIVE generation commands, and delivery checklists for short-form commerce content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can incur cost and may upload local reference media.

Mitigation: Review prompts, routing mode, model choice, pricing snapshots, and files before running generation commands; use small samples before batch work.

Risk: The workflow stores an API key at ~/.ai-hive/config.json when initialized.

Mitigation: Use environment variables when preferred, keep the config file permission-restricted, and remove or rotate the API key when it is no longer needed.

Risk: Generated ecommerce claims, prices, stock, product performance, testimonials, or platform guidance may be inaccurate or unsupported.

Mitigation: Use only verified product facts and authorized materials, mark uncertain claims for review, and perform human review before publishing or submitting paid generation tasks.

## Reference(s):

- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/product-url-to-tiktok-video-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON task records, scripts, prompts, checklists, and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE image or video generation tasks, upload authorized reference media, poll asynchronous task status, download generated media, and run local ffmpeg edits when the user confirms cost-bearing generation settings.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
