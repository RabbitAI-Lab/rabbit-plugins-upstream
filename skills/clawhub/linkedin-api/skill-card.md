## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profile and organization data, uploading media, accessing Ad Library data, and managing advertising features through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a LinkedIn account through Maton OAuth, retrieve LinkedIn data, publish posts, upload media, and manage advertising resources. The skill is suited for agent-assisted LinkedIn workflows where reads are preferred by default and write operations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn OAuth and Maton API access can expose account capabilities and sensitive credentials if mishandled.

Mitigation: Install only when Maton access is trusted, prefer OAuth over API keys, never print or persist credentials, and request only the scopes needed for the current task.

Risk: Posts, campaign changes, budget updates, connection creation, and deletions can have public, financial, or irreversible effects.

Mitigation: Default to read and list operations, show the exact target and payload, confirm budget and targeting details, and wait for explicit user approval before any create, update, delete, publish, or new connection action.

Risk: The documented endpoints are an intended surface, while the Maton API passthrough can reach other LinkedIn endpoints allowed by the connection.

Mitigation: Verify the endpoint, account, and connection before execution; use the narrowest available OAuth scopes; and apply the same write-confirmation rules to every passthrough call.

Risk: Media upload flows use pre-signed LinkedIn upload URLs and can leak sensitive files if the URL or file choice is wrong.

Mitigation: Verify upload URLs point to LinkedIn, upload only files needed for the task, and avoid broad or sensitive media unless the user has confirmed the exact file.

Risk: LinkedIn responses can include personal or business data such as names, emails, phone numbers, messages, documents, and analytics.

Mitigation: Extract only fields needed for the task and avoid writing raw responses to logs, files, or user-visible output unless the user explicitly requests them.

## Reference(s):

- [LinkedIn Skill on ClawHub](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton Homepage](https://maton.ai)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [LinkedIn Authentication Guide](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include LinkedIn API request guidance, Maton CLI commands, raw HTTP fallback examples, and selected API response fields.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
