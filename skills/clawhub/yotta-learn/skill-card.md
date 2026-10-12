## Description:

Helps agents capture reusable lessons in a shared, categorized knowledge base and retrieve reviewed knowledge across projects and sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to record cross-project methods and pitfalls as reviewable knowledge-base entries, then search verified entries before starting similar work. First use includes choosing a shared knowledge-base location and connecting an agent interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-run activation can persist a machine-wide knowledge base and change agent memory or MCP configuration.

Mitigation: Approve the knowledge-base location, MCP changes, and any machine-level discovery anchor before activation; review their scope for every local agent.

Risk: Optional prompt hooks may run a command on every submitted prompt.

Mitigation: Leave the hooks disabled unless their per-prompt execution is acceptable and review the hook configuration before enabling it.

Risk: A shared knowledge base could expose sensitive or project-specific information to other local agents.

Mitigation: Keep secrets and personal data out of shared entries, keep project-only details in project files, and review entries before marking them verified.

Risk: Unpinned npx installations can fetch a different package version later.

Mitigation: Pin the package version when installing through npx.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-learn)
- [Knowledge-base reference](references/kb.md)
- [Activation and hooks reference](references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and commands; knowledge-base entries are Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries progress from draft through review to verified; searches return verified entries by default.]

## Skill Version(s):

0.6.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
