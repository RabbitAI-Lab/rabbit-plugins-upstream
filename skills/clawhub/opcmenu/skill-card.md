## Description:

在独行录（opcmenu.com）查合作需求、主理人、产品和报名机会，并处理本人报名、私信和主办方工作台。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yzlee](https://clawhub.ai/user/yzlee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to opcmenu for public discovery of collaboration needs, creators, products, services, funding, and signup opportunities. With user authorization, it supports account workflows such as signups, private messages, organizer review, profile updates, and daily briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized account actions may read or change real opcmenu data, send messages, submit signups, modify organizer activity, export CSVs, disclose contact information, or spend chat credits.

Mitigation: Use anonymous public browsing where possible, require user authorization for account or write actions, and confirm sensitive actions such as contact disclosure, CSV export, organizer bulk review, and chat-credit redemption before execution.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Connection and authentication](artifact/references/connection.md)
- [Signup and organizer workflows](artifact/references/signup.md)
- [Collaboration, positioning, and brief workflows](artifact/references/workflows.md)
- [opcmenu connection page](https://opcmenu.com/connect)
- [opcmenu public OpenAPI description](https://api.opcmenu.com/openapi.yaml)
- [opcmenu agent navigation](https://opcmenu.com/llms.txt)
- [ClawHub skill page](https://clawhub.ai/yzlee/skills/opcmenu)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, JSON, YAML, and task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate remote MCP tool calls when the host and user authorization allow it.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
