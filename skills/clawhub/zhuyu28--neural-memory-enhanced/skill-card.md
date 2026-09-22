## Description:

Neural Memory Enhanced provides associative memory with spreading activation for persistent recall across agent sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhuyu28](https://clawhub.ai/user/zhuyu28)

### License/Terms of Use:


## Use Case:

Developers and external agent users use this skill to retain decisions, facts, errors, preferences, TODOs, and recent context across sessions through local associative memory tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist conversation details across sessions, including secrets, personal data, regulated information, or client and business details.

Mitigation: Use an isolated environment and store only information that is approved for local retention.

Risk: The release installs unpinned external package code and initialization may change agent configuration.

Mitigation: Pin and verify the neural-memory package version, then inspect configuration changes made by nmem init before enabling the memory server.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhuyu28/skills/neural-memory-enhanced)
- [NeuralMemory GitHub project](https://github.com/nhadaututtheky/neural-memory)
- [ClawHub publisher profile](https://clawhub.ai/user/zhuyu28)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of local memory tools and MCP configuration; persisted memory content is stored outside the rendered response.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
