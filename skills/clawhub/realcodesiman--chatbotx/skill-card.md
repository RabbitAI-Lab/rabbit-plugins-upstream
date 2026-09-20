## Description:

Manage contacts, conversations, broadcasts, flows, sequences, appointments, minigames, and every other ChatbotX workspace resource from the command line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[realcodesiman](https://clawhub.ai/user/realcodesiman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and AI agents use this skill to configure and run the ChatbotX CLI for workspace administration, messaging, analytics, automation, integrations, and related ChatbotX resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to use a powerful ChatbotX workspace API key for deletes, bulk changes, broadcasts, message sends, admin changes, integration changes, and AI/MCP server changes.

Mitigation: Use a least-privilege API key and require explicit confirmation before destructive, bulk, messaging, administrative, integration, or AI/MCP server operations.

Risk: Allowing self-signed certificates can bypass normal TLS certificate validation.

Mitigation: Use CHATBOTX_ALLOW_SELF_SIGNED_CERT or --allowSelfSignedCert only for isolated local development.

## Reference(s):

- [ChatbotX Skill on ClawHub](https://clawhub.ai/realcodesiman/skills/chatbotx)
- [ChatbotX CLI Homepage](https://github.com/ChatbotXIO/ChatbotX/tree/main/apps/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, CLI examples, and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands normally return JSON and require a configured ChatbotX API key and API URL.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
