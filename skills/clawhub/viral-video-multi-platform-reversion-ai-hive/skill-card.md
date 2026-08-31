## Description:

This skill helps Chinese social and commerce content teams turn a master or reference video into platform-specific scripts, prompts, AI-HIVE generation commands, and review checklists for Douyin, Xiaohongshu, WeChat Channels, and TikTok.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content operations teams, MCNs, and brand marketing teams use this skill to adapt authorized video concepts into original platform-specific short-video plans, prompts, commands, task records, and acceptance checks. It is intended for commercial social, ecommerce, advertising, product seeding, short-drama, and comic-video workflows where human review confirms claims, rights, routing, and budget before generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation may upload selected media and incur costs.

Mitigation: Use only authorized source material, review prompts and routing before submitting generation jobs, and confirm budget-sensitive settings before execution.

Risk: API keys could be exposed through logs, screenshots, repositories, or shared files.

Mitigation: Use placeholders in examples, keep API keys in environment variables or the local AI-HIVE config file, and avoid echoing or committing credentials.

Risk: Generated marketing content can contain unsupported claims, misleading testimonials, or platform-specific compliance issues.

Mitigation: Require factual source material for product, brand, price, performance, service-scale, and financing claims, and keep human review in the acceptance checklist.

Risk: Reference-video adaptation can become too close to protected source material or imply unauthorized endorsement.

Mitigation: Retain only abstract structure and pacing, rewrite people, scenes, dialogue, visuals, CTA, and style, and stop at abstract guidance when rights to reference material are not established.

Risk: Local video edits and downloads can overwrite or transform media files unexpectedly.

Mitigation: Preserve original inputs, write outputs to explicit paths, inspect ffmpeg commands before execution, and review generated file locations after task polling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/viral-video-multi-platform-reversion-ai-hive)
- [AI-HIVE chat and API key entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples, JSON task records, generated media file paths, and concise review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON blueprint files, upload selected media to AI-HIVE, poll asynchronous generation tasks, download generated files, and run deterministic ffmpeg edits when the user chooses to execute commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
