## Description:

Turns authorized customer interview material into a Chinese production workflow for B2B case-study videos, including story structure, testimonial excerpts, scripts, AI-HIVE generation commands, and QA checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and customer-success teams use this skill to turn authorized customer interviews, brand facts, and release-channel constraints into customer case-video plans, scripts, prompts, editing commands, and acceptance checks. It helps agents preserve evidence from real interviews while planning optional AI-HIVE media generation or local video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-selected interview, image, video, or audio files to AI-HIVE.

Mitigation: Use only licensed or approved customer materials, remove private or sensitive data before upload, and confirm that the chosen AI-HIVE workflow is appropriate for the content.

Risk: The init flow can store an AI-HIVE API key locally.

Mitigation: Prefer environment variables for short-lived use, keep any local key file private, and avoid including API keys in logs, screenshots, prompts, or version control.

Risk: Generation tasks may incur cost and can create unsupported marketing or testimonial claims if inputs are not reviewed.

Mitigation: Review prompts, model routing, pricing snapshots, factual claims, customer permissions, and acceptance checks before submitting generation jobs or publishing outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/customer-interview-case-video-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON blueprints and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task records, pricing snapshots, model routing choices, task IDs, status summaries, and local file paths when the user runs the bundled tools.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
