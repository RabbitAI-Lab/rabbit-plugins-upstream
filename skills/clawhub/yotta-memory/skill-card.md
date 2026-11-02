## Description:

Yuanyi (yotta-memory) gives AI agents persistent, file-based memory across conversations, with shared facts and owner-isolated private memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to restore context between sessions, save important facts, preferences, boundaries, and commitments, and organize or review a local memory store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy and permission flaws may expose sensitive memories or make shared stores unsafe.

Mitigation: Wait for privacy and permission fixes before storing sensitive memories or sharing a store.

Risk: Remote access to the memory viewer can expose stored information.

Mitigation: Keep the viewer local and stop it after use; use encrypted transport for remote access.

Risk: Identity removal can delete private memories and related credentials.

Mitigation: Retain tested backups before identity removal.

Risk: Memory entries may contain tokens or other sensitive material.

Mitigation: Keep tokens out of memory and avoid private distillation.

## Reference(s):

- [Project repository](https://github.com/YottaMeta/yotta-memory)
- [FAQ](references/faq.md)
- [Protocol reference](references/protocol.md)
- [Provider protocol reference](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.23.2 (source: SKILL.md frontmatter, package.json, skill-manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
