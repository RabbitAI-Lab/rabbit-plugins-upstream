## Description:

This skill helps short-drama and comic-drama teams plan dialogue, narration, subtitles, story assets, shot prompts, and AI-HIVE image or video generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, short-drama studios, comic-drama teams, brands, ecommerce merchants, traffic-buying teams, and overseas-release teams use this skill to turn project goals into production briefs, asset plans, prompt-ready shot work, generation commands, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key and can store it in local configuration.

Mitigation: Use a scoped key where available, keep it out of public files and screenshots, and rotate or revoke it if exposed.

Risk: Selected local media can be uploaded to AI-HIVE or object storage for generation tasks.

Mitigation: Upload only media the user is allowed to process, and avoid confidential, sensitive, or unlicensed source material.

Risk: Generation tasks may create API costs or download generated files locally.

Mitigation: Review pricing and task settings before submission, preserve task IDs for retries, and use --no-download when only task metadata is needed.

Risk: Generated drama, brand, or ecommerce content can contain inaccurate facts, unauthorized likenesses, or rights-sensitive references.

Mitigation: Verify brand facts, product claims, likeness rights, music, images, scripts, and platform safety requirements before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-dialogue-voiceover)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash examples, Python script outputs, and JSON configuration or blueprint files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE generation tasks, poll task status, upload selected media, and optionally download generated image or video outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
