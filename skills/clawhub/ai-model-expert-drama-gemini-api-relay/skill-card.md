## Description:

Helps AI platform teams, enterprise developers, content studios, and ecommerce technical teams organize authorized model interfaces into a unified AI-HIVE entry point for key management, routing, quotas, audit records, and asynchronous image or video tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, AI platform operators, enterprise engineering teams, and content production teams use this skill to plan a governed Gemini or Google AI API relay workflow and run AI-HIVE connectivity checks. It produces gateway blueprints, setup guidance, and executable commands for model discovery, media upload, image or video generation, task polling, and result download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is described as a Gemini relay, while server security evidence says it can run AI-HIVE image and video workflows.

Mitigation: Review the skill before deployment and install it only when AI-HIVE image or video generation is expected.

Risk: Commands may store an AI-HIVE API key and submit paid generation tasks.

Mitigation: Use a limited and revocable key, monitor balance and usage charges, and require explicit confirmation before init, upload, or generate commands.

Risk: Media upload and generation commands can send local files or prompts to AI-HIVE.

Mitigation: Avoid uploading sensitive media and review prompts, files, and task parameters before execution.

Risk: The agent configuration allows implicit invocation.

Mitigation: Consider disabling implicit invocation or requiring explicit user approval for commands that configure keys, upload files, or submit generation jobs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-gemini-api-relay)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE API requests for model lookup, media upload, generation, task polling, and result downloads when executed with a configured API key.]

## Skill Version(s):

1.0.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
