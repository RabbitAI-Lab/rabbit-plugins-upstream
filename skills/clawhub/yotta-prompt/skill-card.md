## Description:

元引 yotta-prompt helps agents clarify vague user requests by offering candidate intent directions, asking for goal/scope/output/constraint details, and producing ready-to-run prompts that can route to matching YottaMeta skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill when a request is vague, underspecified, or framed as a single phrase. The skill guides the agent through intent clarification and returns a prompt or skill-routing suggestion that the user can run directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to make it permanent and always active without explicit user confirmation.

Mitigation: Enable the skill only when a session-start prompt-routing helper is desired, and do not add it to permanent memory, startup prompts, or persistent skill lists without user approval.

Risk: Persistent use could cause private or sensitive clarification details to be stored in long-term memory.

Mitigation: Do not store private or sensitive information in long-term memory unless the user intentionally chooses that behavior.

## Reference(s):

- [Scenario walkthroughs](references/scenarios.md)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-prompt)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-prompt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON with prompt text, candidate intent directions, skill mappings, and optional install commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Clarification output is local/offline and may include self-contained prompts that work without installing additional YottaMeta skills.]

## Skill Version(s):

0.1.0 (source: frontmatter, CHANGELOG, package.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
