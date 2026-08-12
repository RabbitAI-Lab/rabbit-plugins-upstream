## Description:

MCP Skill: read OPC policy news for solo entrepreneurs and self-employed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP server to let an AI assistant query OPC policy information for one-person companies, sole proprietors, freelancers, and self-employed workers. It supports filtering policy results by city, category, keyword, page, and page size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool responses include unsolicited promotional text and an external group link.

Mitigation: Review responses before relying on or redistributing them, especially in professional or customer-facing contexts.

Risk: The OPC API key is sensitive and policy search parameters are sent to the configured OPC API service.

Mitigation: Store OPC_API_KEY only in private client configuration, avoid sharing real keys in examples, and review what query data is acceptable to send.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-1jkgz8e3)
- [OPC service site](https://mrkjai.com)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Plain text or Markdown policy list with titles, city, category, publication date, and links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPC_API_KEY and sends query filters to the configured OPC API service.]

## Skill Version(s):

0.1.0 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
