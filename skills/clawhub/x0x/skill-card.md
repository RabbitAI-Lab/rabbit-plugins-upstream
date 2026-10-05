## Description:

Guides agents in using x0x for encrypted peer-to-peer messaging, group collaboration, and shared data across computers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jimcollinson](https://clawhub.ai/user/jimcollinson)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set up x0x networking and coordinate agents through direct messages, encrypted groups, and shared task or key-value data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating x0x runs a persistent local networking daemon.

Mitigation: Install only when persistent networking is intended; use a verified or pinned release and disable self-update or autostart if unwanted.

Risk: Exposing the REST API or durable API token could grant broad control over the daemon.

Mitigation: Keep the API bound to loopback unless TLS and access controls are added; protect the durable token as an admin credential and prefer scoped rider or session tokens for agents.

## Reference(s):

- [x0x ClawHub release](https://clawhub.ai/jimcollinson/skills/x0x)
- [x0x security documentation](https://github.com/saorsa-labs/x0x/blob/main/docs/security.md)
- [x0x API reference](https://github.com/saorsa-labs/x0x/blob/main/docs/api-reference.md)
- [Linux x64 release archive (installation metadata)](https://github.com/saorsa-labs/x0x/releases/latest/download/x0x-linux-x64-gnu.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls]

**Output Format:** [Markdown with shell commands and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed x0x daemon for networking operations.]

## Skill Version(s):

0.46.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
