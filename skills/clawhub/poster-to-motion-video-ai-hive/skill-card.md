## Description:

This skill helps creative, ecommerce, advertising, and social media teams turn authorized static poster assets into motion-video production plans, prompts, AI-HIVE generation commands, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative, ecommerce, advertising, and social media users use this skill to plan and execute Chinese poster-to-motion-video workflows from authorized materials. The skill produces reviewable briefs, shot and prompt guidance, runnable AI-HIVE commands, task tracking details, and platform-oriented quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-selected media may be uploaded to AI-HIVE during generation workflows.

Mitigation: Use only media the user is authorized to process and avoid uploading sensitive or restricted assets unless that transfer is approved.

Risk: Generation calls may incur costs after task submission.

Mitigation: Review the prompt, model, routing mode, and pricing snapshot before execution; run small samples before batch jobs.

Risk: The skill can store and use an AI-HIVE API key locally.

Mitigation: Prefer environment variables or the provided init flow with restricted file permissions, avoid logging secrets, and rotate any exposed key.

Risk: Generated commercial content may contain incorrect claims or insufficient rights clearance.

Mitigation: Require human review for product facts, legal disclaimers, trademarks, likeness rights, platform rules, and any claim about performance or outcomes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/poster-to-motion-video-ai-hive)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON records and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON briefs, submit AI-HIVE generation tasks, upload user-selected media, and download generated image or video files when the user confirms execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
