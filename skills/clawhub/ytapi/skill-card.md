## Description:

Helps agents retrieve YouTube transcripts, video details, search results, channels, and playlists through YTAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ytapi](https://clawhub.ai/user/ytapi)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching YouTube videos or creators use this skill to find content, read or summarize captions, and inspect channels and playlists. It can also help when direct YouTube fetching is blocked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube queries, URLs, channel identifiers, and any signup email may be sent to YTAPI.

Mitigation: Confirm that the user is comfortable sharing this information before making requests or starting signup.

Risk: The setup flow may create an account and store an API key for future sessions without clear consent.

Mitigation: Ask before creating an account; prefer user-managed key creation and scoped secret storage over shell profiles or agent-wide configuration.

## Reference(s):

- [YTAPI skill listing](https://clawhub.ai/ytapi/skills/ytapi)
- [YTAPI homepage](https://ytapi.dev)
- [YTAPI API documentation](https://docs.ytapi.dev)
- [API key setup](artifact/references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data, Guidance]

**Output Format:** [Plain text, Markdown, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped captions and subtitle formats are available; some requests consume credits.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
