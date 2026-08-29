## Description:

Helps creators, directors, and merchants turn Seedance 2.5 video ideas into T2V, I2V, and R2V prompts, editing or extension guidance, AI-HIVE generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, directors, merchants, and content operators use this skill to plan Chinese Seedance 2.5 video workflows for ecommerce, advertising, marketing, short drama, comics, livestream commerce, and social content. It produces reviewable plans first, then can help prepare AI-HIVE API commands for media upload, model configuration, routed generation, polling, download, and validation after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make billable AI-HIVE API calls for media generation.

Mitigation: Review prompts, model routing, and pricing snapshots before generation; require confirmation before submitting generation tasks and start with a small sample for batch work.

Risk: The workflow can upload user-selected images, video, or audio to AI-HIVE.

Mitigation: Upload only media the user is authorized to use and avoid copyrighted, private, trademarked, or sensitive material without confirmed rights and applicable review.

Risk: The AI-HIVE API key could be exposed through logs, screenshots, or repositories.

Mitigation: Use environment variables or a local config file for credentials, keep placeholders in examples, and do not echo real keys in prompts, outputs, logs, screenshots, or committed files.

Risk: Generated commercial video content can include misleading product, performance, or endorsement claims.

Mitigation: Keep factual claims grounded in user-provided evidence, avoid guarantees about sales or platform outcomes, and validate final content against brand, platform, privacy, and advertising requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-prompt-expert-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls, files]

**Output Format:** [Markdown with inline bash commands and optional JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create blueprint JSON, upload authorized media, submit asynchronous AI-HIVE generation tasks, poll task status, and download generated media when configured with an API key.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
