## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profile and organization information, accessing advertising features, and calling LinkedIn APIs through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to LinkedIn through Maton, retrieve profile, organization, ad, job, and analytics data, and prepare or execute user-approved LinkedIn write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the user's LinkedIn account through OAuth or API-key authentication.

Mitigation: Use OAuth where possible, review granted scopes before use, and revoke unused LinkedIn connections when finished.

Risk: LinkedIn write operations can publish content, modify campaigns, change budgets, or delete resources.

Mitigation: Approve writes only after checking the exact post, campaign, budget, account, or deletion target.

Risk: Advertising operations can have financial or compliance impact.

Mitigation: Confirm campaign budgets, targeting criteria, and applicable policy requirements before executing advertising changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [LinkedIn Authentication Guide](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, Python, and TypeScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, OAuth or API-key authentication, LinkedIn version headers, and explicit user confirmation for writes.]

## Skill Version(s):

1.1.0 (source: release evidence; artifact metadata version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
