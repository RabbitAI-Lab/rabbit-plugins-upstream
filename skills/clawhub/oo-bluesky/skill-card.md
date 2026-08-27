## Description:

Bluesky (bsky.social) connector for reading profiles, timelines, and posts, and creating authenticated text posts through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Bluesky through an OOMOL-connected account, including profile lookup, home timeline reading, post search, and confirmed text posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create Bluesky text posts from the authenticated account.

Mitigation: Confirm the exact post text and intended account impact with the user before running any write action.

Risk: First-time setup may require installing the oo CLI, signing in to OOMOL, and connecting a Bluesky account.

Mitigation: Only perform setup after an auth, connection, or missing-command failure, and ensure the user understands the account connection step before proceeding.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-bluesky)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Bluesky](https://bsky.social)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON data with meta.executionId when executed through the oo CLI.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
