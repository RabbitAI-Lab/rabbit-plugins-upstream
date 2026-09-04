## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profile and organization data, accessing media, advertising features, and other LinkedIn API capabilities through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to access LinkedIn through the Maton CLI or SDK, including profile lookup, organization data, posts, media uploads, public ad-library queries, and marketing operations. It is most appropriate when the user has a valid Maton account and has explicitly authorized the needed LinkedIn connection and scopes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated LinkedIn access can expose profile, organization, posting, media, analytics, and advertising capabilities for the connected account.

Mitigation: Install only when this access is acceptable, prefer OAuth over API keys, grant the narrowest LinkedIn scopes needed, and revoke unused connections promptly.

Risk: Publishing posts, deleting resources, creating connections, or changing advertising budgets and campaigns can affect public content, account state, reputation, or spend.

Mitigation: Default to read and list calls, verify the target account or connection, show the user the request body or key parameters, and require explicit confirmation before any write or destructive operation.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, command lines, files, shell history, or pasted output.

Mitigation: Use the Maton CLI credential store when possible, never print or persist credentials, avoid command-line secrets, and send Maton API keys only to api.maton.ai.

Risk: LinkedIn API responses and external content may include untrusted text that attempts to redirect subsequent actions.

Mitigation: Treat fetched content as data, not instructions; never let API response text select endpoints, recipients, shell commands, or follow-up actions without user intent and validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, JSON request and response examples, and optional Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a valid LinkedIn OAuth connection or Maton API key; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
