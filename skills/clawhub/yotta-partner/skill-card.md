## Description:

Yuanban is a human-AI collaboration protocol skill that gives agents a repeatable flow for context briefs, plan-first execution, milestone delivery, verification, handover anchors, and experience reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to structure complex or long-running human-AI work with explicit context, approval gates, evidence-based verification, and cross-session handover. It is intended for collaboration productivity and does not provide marketing, operations, trading, or domain-specific professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to load at session start and may influence future agent behavior across tasks.

Mitigation: Install it only when a persistent collaboration protocol is desired, and review the always-load behavior before use in sensitive workspaces.

Risk: The artifact asks agents to register the skill in permanent memory and to write project state or memory for long-running work.

Mitigation: Require explicit user approval before permanent-memory registration or any project or memory write, and remove those instructions if they do not match the workspace policy.

Risk: Installation commands can change user-level agent skill directories.

Mitigation: Prefer pinned package/install commands and review the target directory before installing.

## Reference(s):

- [Collaboration Protocol](references/collaboration_protocol.md)
- [Exception Playbook](references/exception_playbook.md)
- [Walkthroughs](references/walkthroughs.md)
- [FAQ](references/faq.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-partner)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with templates, checklists, and optional installation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-start collaboration protocol; no runtime, daemon, network calls, MCP tools, or credential environment variables are evidenced.]

## Skill Version(s):

0.2.0 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
