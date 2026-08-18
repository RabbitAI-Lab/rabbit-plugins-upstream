## Description:

Helps agents create AI music outputs by optimizing prompts, applying style controls, and guiding production-ready audio generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and multimedia producers use this skill to generate or refine AI music prompts, style settings, and audio-production guidance for content creation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and command-execution authority that is not clearly scoped to music generation.

Mitigation: Install only in trusted or sandboxed agent environments, review proposed commands and file writes before execution, and prefer a version with documented allowed commands and file locations.

Risk: Music generation workflows may require API credentials or external service access.

Mitigation: Store API keys in environment variables, avoid committing credentials, and confirm the intended provider and network destination before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/music-generation)
- [SkillHub homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown and JSON-style structured responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include style settings, generation mode, quality notes, and API-key setup guidance.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
