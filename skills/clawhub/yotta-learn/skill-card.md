## Description:

Helps agents capture, review, and retrieve reusable cross-project knowledge in a shared, categorized knowledge base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users capture transferable methods, lessons, and tutorials as drafts, review them, and search verified entries across projects and sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-run setup may persistently change agent memory and MCP configuration without separate clear approval for each change.

Mitigation: Inspect and approve each proposed memory or configuration change; try the manual CLI before enabling MCP integration.

Risk: A machine-wide knowledge base and broad prompt hooks may expose or propagate private information across agents and projects.

Mitigation: Avoid optional broad prompt hooks unless needed, and keep secrets, credentials, sensitive personal data, and private project details out of the shared knowledge base.

Risk: Installing an unpinned npm release may fetch different code later.

Mitigation: Pin the npm package version when installing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage listed in ClawHub metadata](https://github.com/YottaMeta/yotta-learn)
- [Knowledge-base reference](references/kb.md)
- [FAQ](references/faq.md)
- [Hook setup](references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and knowledge-base entries; CLI or MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries start as drafts; reviewed entries can be searched across agents.]

## Skill Version(s):

0.6.4 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
