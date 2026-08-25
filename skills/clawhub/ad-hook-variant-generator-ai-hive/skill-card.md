## Description:

Creates ad-hook variant matrices and short-video production workflows for Chinese ecommerce and social advertising, with optional AI-HIVE video generation through reviewed API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing teams, short-video buyers, directors, and commerce content teams use the skill to turn product facts, audience pain points, platform constraints, historical hooks, and prohibited claims into hook matrices, scripts, prompts, AI-HIVE generation commands, and review checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation calls may incur charges after the user confirms task parameters.

Mitigation: Show the final prompt, mode, routing choice, and pricing snapshot before submitting generation tasks; start with a small sample for batch work.

Risk: Reference images, videos, audio, logos, or claims may be unlicensed, unsupported, or unsuitable for the target platform.

Mitigation: Require users to confirm usage rights and source-backed product facts; mark uncertain claims for review and avoid unlicensed replication or platform-evasion guidance.

Risk: The skill uses an AI-HIVE API key and may upload user-selected media or download generated results.

Mitigation: Use placeholder keys in examples, avoid logging or storing real API keys in shared files, upload only selected media, and keep generated outputs in explicit local output paths.

## Reference(s):

- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)
- [ClawHub skill listing](https://clawhub.ai/wubin1836/skills/ad-hook-variant-generator-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses with inline shell commands and JSON task records; optional local image or video files from AI-HIVE generation tasks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include production blueprints, storyboard scripts, prompt sets, model or routing choices, pricing snapshots, task IDs, status checks, downloaded output locations, and acceptance checklists.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
