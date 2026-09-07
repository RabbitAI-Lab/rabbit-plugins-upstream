## Description:

Guide for using wjx-cli (Wenjuanxing CLI) to create surveys, query responses, analyze data, and manage contacts, departments, and sub-accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orzwq](https://clawhub.ai/user/orzwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to let an agent install and configure wjx-cli, create Wenjuanxing surveys, retrieve responses, analyze NPS/CSAT data, and manage contacts or accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade global npm packages and may fall back to sudo for installation.

Mitigation: Confirm installs and upgrades with the user before running package commands, and avoid privileged installation unless the user explicitly approves it.

Risk: The skill handles Wenjuanxing API keys and can generate SSO URLs that provide account access.

Mitigation: Treat API keys and SSO URLs as secrets, avoid echoing them in chat or logs, and rotate or remove stored credentials after use when appropriate.

Risk: The skill can modify or delete live survey, response, contact, department, tag, admin, and account data.

Mitigation: Require explicit confirmation before destructive or account-changing operations, and report exact success and failure counts for batch actions.

Risk: Incorrect pagination, response counts, or public survey links can mislead users about live survey state.

Mitigation: Use structured JSON responses, server-provided totals, and API-returned URL components instead of table output or guessed links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orzwq/skills/wjx-cli-use)
- [Survey commands reference](references/survey-commands.md)
- [Response commands reference](references/response-commands.md)
- [Analytics commands reference](references/analytics-commands.md)
- [Contacts, departments, admins, tags, accounts, and SSO reference](references/contacts-commands.md)
- [JSONL question types reference](references/question-types.md)
- [Formula helper](references/formula-helper.md)
- [Node.js installation guide](references/install-nodejs.md)
- [Wenjuanxing homepage](https://www.wjx.cn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSONL, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide live Wenjuanxing operations; API keys and generated SSO URLs should not be exposed in chat, logs, or files.]

## Skill Version(s):

0.4.2 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
