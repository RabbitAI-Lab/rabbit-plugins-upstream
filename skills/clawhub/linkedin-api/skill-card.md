## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profiles and organizations, accessing advertising features, uploading media, and using LinkedIn platform APIs through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve LinkedIn profile, organization, advertising, and public ad library data, and to prepare LinkedIn posts or media operations through Maton after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a connected LinkedIn account through Maton, including posting, advertising-management, delete, connection, and media-upload actions.

Mitigation: Install only when this access is acceptable; default to read/list operations and require explicit confirmation with the target resource, payload, budget, or file path before any high-impact action.

Risk: The security evidence flags a mismatch between the skill saying local execution is out of scope and later providing a Python video-upload example.

Mitigation: Treat local Python upload execution as exceptional; allow it only for a specific local video file chosen by the user and never let LinkedIn response content decide what code or file is executed.

Risk: The raw HTTP fallback uses a Maton API key that can leak through logs, shell history, environment inheritance, or process listings.

Mitigation: Prefer OAuth through the Maton CLI; if raw HTTP is unavoidable, check only key presence, avoid printing or persisting the key, feed authorization on stdin, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [byungkyu Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [LinkedIn API Overview](https://learn.microsoft.com/en-us/linkedin/)
- [Share on LinkedIn Guide](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin)
- [LinkedIn Profile API](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api)
- [LinkedIn Authentication Guide](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)
- [LinkedIn Ad Library API](https://www.linkedin.com/ad-library/api/)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Networked LinkedIn calls require Maton authentication, a connected LinkedIn account, and user confirmation before write, campaign, delete, connection, or media-upload actions.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
