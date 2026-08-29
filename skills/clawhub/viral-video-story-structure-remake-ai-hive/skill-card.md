## Description:

Helps brand content teams, short-drama writers, and advertising creatives turn authorized reference material and brand facts into original short-video story beats, conflict escalation, reversal points, brand integration, storyboards, prompts, and AI-HIVE generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand content teams, short-video writers, advertising creatives, and agent operators use this skill to analyze authorized viral-video story structures and produce differentiated scripts, shot plans, prompts, and review checklists for ecommerce, advertising, marketing, short-drama, and social content workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can require an AI-HIVE API key.

Mitigation: Use environment variables or the local config path described by the skill, keep real keys out of prompts, logs, screenshots, and project files, and use placeholders in shared examples.

Risk: Reference media may be uploaded to AI-HIVE or object storage.

Mitigation: Use only media the user is authorized to process, confirm rights before upload, and avoid uploading private or sensitive assets unless approved.

Risk: Generation calls can incur costs.

Mitigation: Review prompts, model configuration, routing mode, and price snapshots before submitting generation jobs; run small samples before batch work.

Risk: Story-structure remakes can become too similar to protected source material or can imply unsupported product claims.

Mitigation: Keep only abstract structure and pacing, rewrite characters, dialogue, scenes, and visual style, and require factual support for brand, product, testimonial, pricing, and performance claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/viral-video-story-structure-remake-ai-hive)
- [AI-HIVE chat and API key entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured Chinese workflow sections, inline shell commands, JSON file outputs, prompts, and task records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local blueprint JSON, ffmpeg command output, AI-HIVE request parameters, task IDs, status records, and download locations after user review.]

## Skill Version(s):

1.0.0 (source: evidence.release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
