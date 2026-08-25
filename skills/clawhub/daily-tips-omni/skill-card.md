## Description:

Daily AI agent optimization tips, tricks and self-improvement strategies for reducing costs, improving performance, managing memory, and learning automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use this skill to receive daily optimization guidance, search cost, speed, memory, skills, and automation tips, and generate weekly summaries of saved tips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores saved and skipped tip preferences in local JSON files under the skill directory.

Mitigation: Review local preference files if using the skill in shared environments and avoid storing sensitive notes in saved tip data.

Risk: Optional community-feed behavior depends on a locally available reddit-readonly helper.

Mitigation: Review the helper skill before enabling community-feed or scheduled use, and rely on the built-in curated tips if the helper is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adelpro/skills/daily-tips-omni)
- [Publisher profile](https://clawhub.ai/user/adelpro)
- [Cron Optimization](references/cron-optimization.md)
- [Model Selection](references/model-selection.md)
- [openclaw-agent-optimize](https://clawhub.ai/phenomenoner/openclaw-agent-optimize)
- [openclaw-token-optimizer](https://clawhub.ai/phenomenoner/openclaw-token-optimizer)
- [memory-setup](https://clawhub.ai/phenomenoner/memory-setup)
- [compound-engineering](https://clawhub.ai/phenomenoner/compound-engineering)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-like CLI text with optional JSON cron configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores saved and skipped tip preferences as local JSON files under the skill directory.]

## Skill Version(s):

1.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
