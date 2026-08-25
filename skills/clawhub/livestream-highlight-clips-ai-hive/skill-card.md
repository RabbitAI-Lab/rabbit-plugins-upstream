## Description:

Turns livestream replay highlight-clipping requests into a production workflow with candidate timecodes, clip scripts, subtitle notes, cover guidance, vertical-video commands, and optional AI-HIVE generation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, livestream commerce teams, brand store teams, and agent users use this skill to turn authorized livestream replays, transcripts, product timelines, platform targets, and duration constraints into reviewable highlight-clip plans and delivery commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload selected media and prompts to AI-HIVE and may start paid generation tasks.

Mitigation: Require explicit review of final parameters, route, and cost-relevant settings before uploads, generation, or batch execution.

Risk: Livestream clips can misrepresent source material, unauthorized media, product claims, or user testimonials.

Mitigation: Confirm source-material authorization, preserve the original meaning, mark unverified claims for review, and avoid fabricated endorsements or platform-rule evasion.

Risk: API keys or generated task details could be exposed in chats, logs, screenshots, or repository files.

Mitigation: Use placeholders in examples, keep credentials in environment variables or private config, and review outputs before sharing or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/livestream-highlight-clips-ai-hive)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include candidate highlight timecodes, production briefs, edit commands, AI-HIVE task records, and quality checklists.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
