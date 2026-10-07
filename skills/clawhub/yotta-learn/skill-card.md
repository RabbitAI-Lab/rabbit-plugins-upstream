## Description:

Helps agents capture mistakes, corrections, and insights as reusable learning entries and maintain a searchable, reviewed knowledge base across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users capture and review lessons from failures or corrections, promote useful lessons to agent guidance, and retrieve verified knowledge for later tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent configuration and memory instructions may affect future sessions.

Mitigation: Review hooks and MCP configuration before enabling them, and install only if persistent local learning is desired.

Risk: Stored learnings and knowledge may expose secrets or private source content.

Mitigation: Avoid recording secrets and private source content; review entries before promoting them to agent guidance.

Risk: A future package release could change installed behavior.

Mitigation: Pin the npm package version and review updates before installing.

Risk: The documented local web console may not work in this release because its HTML asset is absent.

Mitigation: Verify the console asset is present before relying on the web interface; use the CLI otherwise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage (listed in release metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-learn)
- [Knowledge base reference](artifact/references/kb.md)
- [Hooks setup reference](artifact/references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown learning and knowledge-base entries, CLI text, and agent setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Learning entries and reviewed knowledge can persist locally across agent sessions.]

## Skill Version(s):

0.4.0 (source: release evidence, frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
