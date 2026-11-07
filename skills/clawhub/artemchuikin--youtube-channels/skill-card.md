## Description:

Reach for this when a YouTube channel is the subject: a pasted @handle or channel URL, a creator's recent uploads, their full catalogue, or a search inside one channel. Also good for keeping an eye on what somebody publishes. Skip it for creating channels or account chores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users can check a YouTube creator's latest uploads, browse the channel catalogue, search within a channel, and monitor publishing activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated CLI signup can turn a crafted email address into local commands.

Mitigation: Create an account through TranscriptOut's website and enter the API key through the runtime's secret prompt; avoid automated CLI signup.

Risk: Requests share channel and search inputs with TranscriptOut and spend credits.

Mitigation: Send only intended inputs, use the latest-uploads endpoint when it is sufficient, and check the remaining credit balance.

Risk: Fallback credential setup stores the API key locally and changes the shell profile.

Mitigation: Prefer the runtime's secret store; otherwise keep the key in the private config file and have the profile read it without containing the key.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs?utm_source=youtube-skills&utm_medium=clawhub&utm_content=youtube-channels)
- [API key setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON API results with agent-written summaries or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Channel results may be paginated; requests consume API credits.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
