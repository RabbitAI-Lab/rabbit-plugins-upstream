## Description:

Provides agent-facing guidance for answering current weather and forecast requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for current weather, forecasts, and related weather details for a specified location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks for broad read, write, and command execution authority beyond weather lookup.

Mitigation: Install only after the publisher narrows behavior to weather-specific actions or documents tightly scoped, user-directed uses for those tools.

Risk: The documentation is inconsistent about whether an API key is required.

Mitigation: Confirm the weather provider and credential requirements before deployment; avoid storing API keys in skill text or source control.

Risk: Broad or unrelated automation claims may cause agents to use the skill outside weather tasks.

Mitigation: Constrain invocation to current weather, forecast, and weather-status requests and review outputs before relying on them for planning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/weather)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-shaped response examples with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include location-specific weather results; source documentation is inconsistent about whether an API key is required.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
