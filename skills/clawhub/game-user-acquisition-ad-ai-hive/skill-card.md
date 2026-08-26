## Description:

Helps mobile game user acquisition and creative teams turn authorized gameplay material, campaign goals, platform constraints, and KPIs into ad concepts, gameplay anchors, hooks, scripts, AI-HIVE generation commands, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketers, and mobile game UA teams use this skill to plan Chinese game acquisition ads, prepare storyboard and prompt deliverables, and run AI-HIVE video generation workflows after reviewing authorization, routing, pricing, and disclosure requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation can involve billable API calls and asynchronous media generation tasks.

Mitigation: Review prompts, routing mode, model configuration, and pricing snapshot before submitting generation commands.

Risk: The workflow may upload media files supplied by the user and download generated files locally.

Mitigation: Use only media the user is authorized to process, confirm media rights before upload, and review output file locations.

Risk: API credentials are required for AI-HIVE calls.

Mitigation: Provide credentials through the documented environment variable or local config and avoid exposing real API keys in prompts, logs, screenshots, or version control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/game-user-acquisition-ad-ai-hive)
- [AI-HIVE web app](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown with inline shell commands, Python examples, JSON task records, and optional generated media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, upload user-provided media to AI-HIVE, submit billable generation tasks, poll task status, and download generated image or video outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
