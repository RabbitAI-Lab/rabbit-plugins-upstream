## Description:

Guides agents in using wjx-cli to create Wenjuanxing surveys, query responses, analyze survey data, and manage contacts, departments, and sub-accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orzwq](https://clawhub.ai/user/orzwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent perform Wenjuanxing survey workflows through wjx-cli, including survey creation, response retrieval, exports, local analytics, and organization contact management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to handle Wenjuanxing API keys and account credentials.

Mitigation: Configure credentials locally or through a secure secret mechanism, avoid pasting secrets into chat, and stop authenticated workflows when API-key errors occur.

Risk: The skill covers high-impact account, SSO, contact, department, administrator, and deletion operations.

Mitigation: Review every destructive or account-management action before execution and confirm successful or failed API responses before reporting outcomes.

Risk: The bundled setup flow can install wjx-cli globally and may fall back to sudo.

Mitigation: Use the global or sudo install path only in environments where package-install risk is accepted; otherwise install and test wjx-cli in an isolated environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orzwq/skills/wjx-cli-use)
- [Wenjuanxing](https://www.wjx.cn)
- [Survey command reference](references/survey-commands.md)
- [Response command reference](references/response-commands.md)
- [Question type reference](references/question-types.md)
- [Analytics command reference](references/analytics-commands.md)
- [Contacts, departments, admins, accounts, and SSO reference](references/contacts-commands.md)
- [Formula helper guide](references/formula-helper.md)
- [Node.js installation guide](references/install-nodejs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSONL examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local JSONL survey definitions, CLI command plans, and configuration guidance; authenticated operations depend on locally configured Wenjuanxing credentials.]

## Skill Version(s):

0.3.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
