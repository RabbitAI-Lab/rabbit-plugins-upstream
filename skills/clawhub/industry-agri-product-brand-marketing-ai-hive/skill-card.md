## Description:

Generates agricultural product brand marketing plans, image and short-video prompts, AI-HIVE generation commands, task records, and review checklists for channels such as Douyin, Xiaohongshu, WeChat Channels, Kuaishou, public accounts, agricultural platforms, and private dealer channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, agricultural brands, stores, agencies, and operators use this skill to plan and produce fact-checked product marketing assets, including audience strategy, content calendars, image matrices, video storyboards, prompts, platform rewrites, AI-HIVE task records, and follow-up metrics. Users are expected to verify product facts, media rights, budget, routing mode, and upload paths before running generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated marketing content could include incorrect claims about origin, variety, year, production method, testing, nutrition, efficacy, price, address, stock, or platform rules.

Mitigation: Require human confirmation of product facts and mark uncertain claims as pending verification before generation or publication.

Risk: Image, video, audio, logo, or person references may be uploaded to AI-HIVE without adequate rights or consent.

Mitigation: Use only authorized reference media and verify consent for people, customer cases, children, residents, vehicles, company examples, logos, and music before upload.

Risk: Generation commands can create billable AI-HIVE tasks and download outputs locally.

Mitigation: Confirm budget, routing mode, pricing snapshot, output directory, and taskId tracking before running generation or polling commands.

Risk: API keys may be stored in a local configuration file if the user chooses the init flow.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable; if using ~/.ai-hive/config.json, keep file permissions restricted and avoid screenshots, logs, or repository commits containing secrets.

Risk: Broad implicit invocation could activate the skill for many agriculture, branding, image, video, or marketing prompts.

Mitigation: Confirm the user intends to use AI-HIVE for agricultural-product marketing assets before running network, upload, or generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/industry-agri-product-brand-marketing-ai-hive)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)
- [Agricultural product marketing industry playbook](references/industry-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands, Python helper scripts, JSON task records, and downloaded image or video assets when AI-HIVE generation is run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform network generation, media upload, model and pricing lookup, task polling, local downloads, and ffmpeg-based video edits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
