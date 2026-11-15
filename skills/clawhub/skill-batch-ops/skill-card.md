## Description:

Coordinates inventory, batch updates, multi-platform publishing, version alignment, and per-item verification across multiple skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this agent to inventory and update three or more agent skills, coordinate publication across platforms, align versions, and verify each item.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow refers to a local SkillHub credentials file and can publish changes across multiple skills and platforms.

Mitigation: Keep credentials in a protected store, avoid printing or copying tokens into skill files or publish payloads, and confirm the target skill list before publishing.

Risk: The skill references an external SkillHub publishing endpoint.

Mitigation: Review the endpoint and its purpose before sending publish requests, and use it only for the intended SkillHub operations.

## Reference(s):

- [SkillHub community publish API](https://api.skillhub.cn/api/v1/community/skills/publish)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown batch status tables, per-item verification results, and skill file updates as applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-item results and failures are recorded for the batch.]

## Skill Version(s):

1.0.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
