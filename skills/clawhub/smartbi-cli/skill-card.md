## Description:

smartbi-cli lets an agent use the @smartbi/cli command-line tool to discover Smartbi BI OpenAPI operations, inspect contracts, prepare requests, and execute analytics, modeling, scheduling, messaging, resource, and permission workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wahsonleung](https://clawhub.ai/user/wahsonleung)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, BI administrators, and analytics operators use this skill to let an agent translate natural-language BI requests into Smartbi CLI discovery, describe, document, and call workflows. It supports Smartbi data queries, AI-assisted analysis, modeling, data source management, scheduled tasks, ETL-style workflows, message pushes, and resource or permission operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad access to Smartbi BI operations, including data queries, modeling, scheduled tasks, message delivery, resources, and permissions.

Mitigation: Review the skill before installing it, grant only least-privilege Smartbi tokens, and confirm each API call before execution.

Risk: The skill stores or uses a local Smartbi token and configuration file.

Mitigation: Protect or restrict the local configuration file and keep token revocation steps available.

Risk: The skill can create scheduled data sends or push BI data through webhooks, email, or messaging channels.

Mitigation: Confirm schedules, activation state, recipients, and data-sharing approval before enabling tasks or sending BI data outside approved channels.

## Reference(s):

- [Smartbi CLI Skill README](README.md)
- [list / search reference](references/discovery.md)
- [describe reference](references/describe.md)
- [call reference](references/call.md)
- [init and configuration reference](references/init.md)
- [multi-environment profile reference](references/profiles.md)
- [strategy reference](references/strategy.md)
- [Domain documentation index](references/doc-index.md)
- [MQL Rhino script template](references/rhino-template.md)
- [scheduled task scenario](scenarios/schedule-task.md)
- [message push scenario](scenarios/push-message.md)
- [ClawHub skill page](https://clawhub.ai/wahsonleung/skills/smartbi-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request-body files, and summarized Smartbi CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create temporary JSON request files for smartbi call workflows and may use a helper script to inject Rhino JavaScript into request bodies.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
