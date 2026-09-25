## Description:

Doubao Chat lets an agent query the Doubao large language model through a free API wrapper that supports internet-connected search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bseye520](https://clawhub.ai/user/bseye520)

### License/Terms of Use:


## Use Case:

Developers and external users can use this skill to send prompts to Doubao from an agent workflow and receive chat responses through a Node.js command-line script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user prompts and a reusable Doubao session credential to an unofficial third-party Vercel endpoint.

Mitigation: Treat DOUBAO_SESSIONID as an account credential, avoid sensitive prompts, and prefer an official scoped API token or official endpoint if available.

Risk: The skill provides limited warning about how prompts and credentials are handled by the third-party service.

Mitigation: Install only when the deployment owner accepts that service receiving prompts and the session identifier.

## Reference(s):

- [Doubao Homepage](https://www.doubao.com)
- [Doubao Free API Chat Completions Endpoint](https://doubao-free-api.vercel.app/v1/chat/completions)
- [ClawHub Skill Page](https://clawhub.ai/bseye520/skills/doubao-chat)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration]

**Output Format:** [Plain text terminal output with Markdown usage examples in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, curl, and DOUBAO_SESSIONID.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
