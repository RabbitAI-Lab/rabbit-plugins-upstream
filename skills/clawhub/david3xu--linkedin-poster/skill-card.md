## Description:

Use when an agent needs to draft and publish LinkedIn text posts, image posts, and Build in Public updates through a configured LinkedIn channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[david3xu](https://clawhub.ai/user/david3xu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to let an agent prepare LinkedIn feed posts with optional image media, then publish them through the authenticated user's LinkedIn account after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish public LinkedIn posts through the configured account.

Mitigation: Confirm the exact platform, text, and media before allowing any post.

Risk: Misconfigured or expired LinkedIn credentials can prevent posting or fail authorization.

Mitigation: Verify channels.linkedin includes a valid access token with w_member_social scope and the correct person URN.

## Reference(s):

- [LinkedIn Poster on ClawHub](https://clawhub.ai/david3xu/skills/linkedin-poster)
- [OpenClaw LinkedIn extension](https://github.com/openclaw/openclaw/tree/main/extensions/linkedin)
- [LinkedIn Post Templates](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires channels.linkedin configuration with a LinkedIn access token and person URN; successful posts are public and tied to the authenticated profile.]

## Skill Version(s):

1.0.0 (source: server release metadata and OpenClaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
