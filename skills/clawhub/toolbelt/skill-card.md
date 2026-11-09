## Description:

Toolbelt helps agents ingest documents, query structured and unstructured data through MCP, and share persistent workspaces across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using MCP-compatible agents can set up Toolbelt to ingest approved documents, ask questions across structured and unstructured data, and share persistent findings with other agents and sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags account-claiming instructions that send account details to Toolbelt's web application, despite a stated MCP-only boundary.

Mitigation: Review the account-claiming request and proceed only if comfortable sending the email address and verification code to the web application.

Risk: The security scan was partial and does not establish that all referenced material was inspected.

Mitigation: Review unresolved local path-like references and related material before installing or following the skill.

## Reference(s):

- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Toolbelt complete documentation](https://toolbelt.ai/llms-full.txt)
- [Toolbelt skill release](https://clawhub.ai/toolbeltai/skills/toolbelt)

## Skill Output:

**Output Type(s):** [Text, Configuration, Shell commands, Guidance]

**Output Format:** [Text and Markdown, including MCP configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the requested setup and data task.]

## Skill Version(s):

1.1.2 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
