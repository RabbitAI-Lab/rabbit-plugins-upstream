## Description:

Connects agents to LinkedIn through Maton-managed OAuth so they can read profile and organization data, publish posts, upload media, and use advertising APIs when granted scopes allow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with LinkedIn accounts through Maton, including profile lookup, organization lookup, post creation, media upload, ad-library search, and marketing API workflows. It is most appropriate when a valid Maton account, network access, and an explicitly authorized LinkedIn connection are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn access is mediated through Maton and can expose profile, organization, post, media, advertising, analytics, and other endpoint data allowed by the connected OAuth scopes.

Mitigation: Review OAuth scopes before connecting, prefer read-only access when possible, and use the narrowest connection needed for the task.

Risk: Write operations can publish public content, delete connections, change campaigns, modify ad accounts, or affect advertising budgets.

Mitigation: Require explicit user confirmation for connection creation and every POST, PUT, PATCH, or DELETE operation, with extra confirmation for deletes, campaigns, budgets, and ad-account changes.

Risk: Raw API-key usage can expose a long-lived Maton credential through environment variables, logs, shell history, or pasted output.

Mitigation: Prefer Maton OAuth login and OS credential storage; when an API key is unavoidable, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: LinkedIn API responses may contain personal data or untrusted external content.

Mitigation: Extract only fields needed for the task, avoid writing raw responses to logs or files, and treat returned content as data rather than instructions.

## Reference(s):

- [ClawHub LinkedIn Skill](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for Maton CLI, raw HTTPS, and SDK-based LinkedIn API workflows; normal outputs may include command examples and API response summaries.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
