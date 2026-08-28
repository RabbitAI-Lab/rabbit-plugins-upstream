## Description:

This skill helps API relay, design-product, AI-application, and ecommerce SaaS teams turn GPT Image 2 and Nano Banana image-generation requests into AI-HIVE workflows, runnable commands, and reviewable delivery checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content operations teams use this skill to plan and run AI-HIVE image or video generation workflows with model selection, reference upload, cost routing, polling, downloads, and acceptance checks. It is aimed at commercial ecommerce, advertising, marketing, social content, short-video, and SaaS production workflows where source-media authorization and review are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit potentially billable AI-HIVE image or video generation jobs.

Mitigation: Confirm prompts, generation mode, routing, budget, and batch size before execution; run a small sample before scaling.

Risk: The skill can upload user-selected media and download generated outputs.

Mitigation: Use only authorized source media and review outputs for copyright, trademark, privacy, and platform-policy issues before publication.

Risk: The init flow can store an AI-HIVE API key locally.

Mitigation: Prefer environment variables for transient use, avoid committing keys or logs, and keep any local config file restricted to the current user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-nano-banana-api-relay-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, Python command examples, JSON task records, and checklist items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, submit AI-HIVE media-generation jobs, upload user-selected media, poll task status, and download generated outputs when the user confirms execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
