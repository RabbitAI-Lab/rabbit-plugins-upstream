## Description:

Helps brands, content teams, short-drama teams, e-commerce teams, and AI search operators turn GEO+AEO brand search-growth goals into structured plans, evidence fields, storyboards, media-generation tasks, and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to plan GEO+AEO brand AI search work, create structured answer and source-card plans, and generate supporting image or video assets through AI-HIVE. It is also useful for short-drama and comic production teams that need reusable project blueprints, storyboards, media prompts, task tracking, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API keys are real credentials and could be exposed if copied into public files, screenshots, or shared repositories.

Mitigation: Use environment variables or a local config file with restricted permissions, and rotate or revoke keys if exposure is suspected.

Risk: Media-generation workflows can upload user-selected files to AI-HIVE.

Mitigation: Upload only assets the user is authorized to send to the service, especially when files contain people, brands, music, scripts, or private business material.

Risk: Generation tasks may incur cost or use model routing that differs from the user's expectation.

Mitigation: Review pricing snapshots, routing mode, model choice, quantity, and output settings before submitting tasks.

Risk: AI search visibility, inclusion, ranking, or citation outcomes may be overstated if treated as guaranteed.

Mitigation: Use confirmed facts, source cards, update dates, and repeatable visibility-audit records; do not promise that third-party models will include, rank, or cite the content.

Risk: Generated content can introduce factual, copyright, likeness, trademark, or platform-safety issues.

Mitigation: Confirm brand and product facts, verify authorization for protected materials or real-person likeness, and review generated outputs before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-geo-aeo-brand-growth)
- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [Artifact Skill Documentation](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON blueprints, local configuration examples, and AI-HIVE task identifiers or generated media file paths when commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image and video workflows require an AI-HIVE API key and may upload user-selected media, submit paid generation tasks, poll task status, and download generated outputs.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
