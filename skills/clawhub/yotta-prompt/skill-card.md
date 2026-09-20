## Description:

元引 yotta-prompt helps agents clarify vague user requests, present candidate intent directions, gather goal, scope, output, and constraint details, then route the clarified task to a suitable YottaMeta skill or self-contained prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and agent developers use this skill when a request is too vague to execute directly. It guides the conversation into a clear task, suggests relevant YottaMeta skills, and produces ready-to-run prompts or local CLI output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to be active at session start and may influence future conversations if a user approves persistent registration.

Mitigation: Require explicit user consent before writing permanent memory, startup configuration, or an always-on skill list entry; document how to remove the persistent registration.

Risk: Installation can run through npx or target multiple agent skill directories, which may broaden where the skill is enabled.

Mitigation: Prefer pinned package versions or manual artifact review before installation, and avoid global or multi-agent installation unless that scope is intentional.

Risk: Intent classification and skill routing may suggest an unsuitable direction for ambiguous input.

Mitigation: Have the agent present candidate directions and obtain user confirmation before executing or routing the clarified task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [Project homepage](https://github.com/YottaMeta/yotta-prompt)
- [FAQ](references/faq.md)
- [Scenario library](references/scenarios.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-prompt)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text guidance, with optional JSON CLI output and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Python 3.8+ standard library; can emit 2-4 candidate intent directions, follow-up questions, self-contained prompt templates, and YottaMeta skill routing suggestions.]

## Skill Version(s):

0.2.2 (source: server release metadata, SKILL.md frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
