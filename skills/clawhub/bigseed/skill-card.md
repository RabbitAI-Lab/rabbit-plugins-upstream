## Description:

Big Seed is an AI diary and life-story skill that helps users save short personal notes, classify them, build a personal profile, and generate memoir-style stories, scripts, reports, and weekly summaries from local diary data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users use Big Seed to capture personal reflections, memories, emotions, and ideas as local diary entries. The skill then helps retrieve those entries, summarize personal patterns, and generate stories, memoir-style narratives, weekly briefings, or creative prompts from the saved material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores sensitive personal diary entries and attachments in a local plaintext data directory.

Mitigation: Use only in trusted local environments, avoid recording secrets or highly sensitive personal details, and review or delete saved entries when needed.

Risk: Default weekly summaries may derive profiles and stories from diary data and push them to a chat destination such as Feishu.

Mitigation: Confirm the delivery destination before use and disable weekly chat delivery if the user does not want automated summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/bigseed)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands and JSON-backed local diary data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local JSON files under memory/bigseed-data and generate scheduled weekly chat summaries when enabled.]

## Skill Version(s):

2.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
