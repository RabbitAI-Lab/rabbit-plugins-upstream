## Description:

Summarizes YouTube videos or recent channel uploads into notes with key points, quotes, and timestamped links using YTAPI transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to turn YouTube videos or a channel's new uploads into concise notes and timestamped takeaways, including when direct YouTube fetching is blocked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account creation and persistent API-key storage can expose a credential to later sessions or other processes.

Mitigation: Create the YTAPI account and key yourself, provide the key through a dedicated secret store or session-scoped mechanism, and avoid shell-profile or broad agent-config storage unless intentional.

## Reference(s):

- [YTAPI documentation](https://docs.ytapi.dev)
- [YTAPI homepage](https://ytapi.dev)
- [API key setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown notes with key points, quotes, and timestamped video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries follow the user's language and flag auto-generated captions when present.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
