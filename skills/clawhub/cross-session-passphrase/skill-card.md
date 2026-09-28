## Description:

Helps an agent pass instructions between sessions on the same local account through registered passphrases and shared memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

All Rights Reserved

## Use Case:

People using parallel agent sessions on the same local account can register a passphrase so another session can locate a specified file or handoff note and report its contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent passphrase-to-action mappings may cause other sessions to read files automatically.

Mitigation: Require explicit consent for each file before registering or using a handoff, and remove unneeded MEMORY.md mappings.

Risk: Workspace logs may contain secrets that a handoff could expose.

Mitigation: Avoid scanning logs containing secrets; review requested files before sharing their contents between sessions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/cross-session-passphrase)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe passphrase-to-action mappings for local shared memory.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release; packaged manifest lists 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
