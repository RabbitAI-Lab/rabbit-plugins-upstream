## Description:

Todoist API integration with managed OAuth for managing tasks, projects, sections, labels, and comments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read, create, update, complete, and organize Todoist tasks, projects, sections, labels, and comments through a managed OAuth gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Todoist access is routed through Maton and can read or change connected Todoist data.

Mitigation: Install only if comfortable with the Maton gateway, prefer OAuth through the Maton CLI, and confirm every write or delete before execution.

Risk: Multiple Maton or Todoist connections can cause actions to run against the wrong account.

Mitigation: Specify the intended connection or profile when multiple accounts exist, especially before any modifying operation.

Risk: The raw MATON_API_KEY fallback exposes a long-lived credential to the local environment.

Mitigation: Use the raw curl fallback only in controlled environments without the CLI, avoid printing or persisting the key, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/todoist-api)
- [Maton Homepage](https://maton.ai)
- [Todoist API v1 Documentation](https://developer.todoist.com/api/v1)
- [Todoist Filter Syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Todoist OAuth Documentation](https://developer.todoist.com/guides/#oauth)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Todoist API request examples and user-confirmation prompts before writes or connection creation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
