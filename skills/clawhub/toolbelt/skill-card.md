## Description:

Toolbelt helps agents connect to a shared workspace for document extraction, hybrid data retrieval, and cross-session collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers use this skill to set up Toolbelt for tasks that need persistent, shared access to documents and structured data through an MCP-compatible agent. It also explains how to connect the agent and use the workspace safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may access MCP configuration and make an account-claim request, which could conflict with the user's expected network or settings access.

Mitigation: Review the MCP settings and account-claim flow before setup; proceed only when those actions are expected.

Risk: Toolbelt share URLs grant access to a workspace to anyone who has the URL.

Mitigation: Share URLs only through channels the user controls and with intended recipients.

## Reference(s):

- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Toolbelt full documentation](https://toolbelt.ai/llms-full.txt)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, API calls]

**Output Format:** [Markdown guidance, JSON configuration examples, and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account setup and client configuration require user confirmation.]

## Skill Version(s):

1.1.7 (source: artifact frontmatter; server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
