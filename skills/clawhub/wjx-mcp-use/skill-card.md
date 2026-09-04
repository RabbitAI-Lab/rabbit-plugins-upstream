## Description:

Guides agents in administering Wenjuanxing (问卷星) surveys, responses, contacts, accounts, analysis workflows, and SSO links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orzwq](https://clawhub.ai/user/orzwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to let an agent help administer a Wenjuanxing account, including creating surveys, forms, exams, and polls; retrieving and analyzing response data; and managing related contacts, accounts, and links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Wenjuanxing account administration, including changes to survey, response, exam, contact, department, and account data.

Mitigation: Install only for agents that are intended to administer a Wenjuanxing account, scope use to relevant survey-management tasks, and use a least-privilege API key where possible.

Risk: Destructive operations may delete surveys, responses, contacts, departments, accounts, participant records, or recycle-bin data.

Mitigation: Require explicit human confirmation and verify target identifiers before deletion, clearing, score modification, or status-changing actions.

Risk: API keys, custom domains, corporate identifiers, and admin SSO links can expose or grant account access if mishandled.

Mitigation: Keep credentials in environment or MCP configuration, avoid exposing them in chat or logs, and require confirmation before generating administrator SSO links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orzwq/skills/wjx-mcp-use)
- [DSL syntax and question types](references/dsl-and-types.md)
- [Survey tool reference](references/tools-survey.md)
- [Response data tool reference](references/tools-response.md)
- [Account, SSO, and analysis tool reference](references/tools-other.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSONL and shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead an agent to call Wenjuanxing account-administration tools when configured with account credentials.]

## Skill Version(s):

0.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
