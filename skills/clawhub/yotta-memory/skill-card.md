## Description:

Helps AI agents retain, retrieve, and organize local memories across sessions with public and private access boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to save, search, and restore long-term context between agent sessions, with separate handling for shared facts and private memories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term memories and local connection credentials may contain sensitive information.

Mitigation: Review what agents save; keep tokens and agent keys out of memories and in protected credential storage.

Risk: Optional LAN serving and autostart can expose the memory service beyond the local machine.

Mitigation: Enable these features only after reviewing access, authentication, and the intended network exposure.

Risk: Optional provider plugins and runtime updates can run additional code or access memory data.

Mitigation: Pin install versions and review plugin commands and accessible data before enabling them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Memory protocol](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown; optional structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and write persistent local memory files.]

## Skill Version(s):

0.22.3 (source: server release, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
