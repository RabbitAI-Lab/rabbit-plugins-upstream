## Description: <br>
Access and manage Gmail emails and Google Tasks through Composio's unified API with tools for sending, searching, creating tasks, and related automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rita5fr](https://clawhub.ai/user/rita5fr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation agents use this skill to discover and invoke Composio tools for Gmail and Google Tasks, including email retrieval, email sending, task creation, and task management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Published live-looking API credentials and account identifiers may expose connected Gmail or Google Tasks accounts. <br>
Mitigation: Do not use the embedded key or account IDs; replace them with scoped credentials and accounts you control before installation or execution. <br>
Risk: The skill can perform sensitive mailbox and task actions, including sending email, deleting email, and bulk-changing tasks. <br>
Mitigation: Limit allowed tools and connected accounts, then require explicit confirmation before any sending, deletion, or bulk modification. <br>
Risk: The security review verdict is suspicious because credentials and personal identifiers are published with operational automation scripts. <br>
Mitigation: Prefer a revised release that removes personal identifiers and validates credential handling before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rita5fr/skills/composio-integration) <br>
- [Composio REST API documentation](https://docs.composio.dev/rest-api/) <br>
- [Composio apps catalog](https://docs.composio.dev/apps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JavaScript examples, and JSON arguments] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute Composio API calls when run with user-provided credentials and connected account IDs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
