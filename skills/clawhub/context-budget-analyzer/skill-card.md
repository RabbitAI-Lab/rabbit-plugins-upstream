## Description:

Analyzes an agent session's context budget, identifies content that may cause context pollution or compaction risk, and recommends practical ways to preserve, structure, externalize, or discard information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to understand how a selected conversation uses its context budget, identify possible sources of context pollution, and plan what to retain before compaction. It provides analysis and recommendations without modifying conversation data or configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation logs may contain sensitive information.

Mitigation: Provide only logs intended for analysis and remove secrets before sharing them.

Risk: Missing or deduplicated usage records can limit conclusions about the complete session.

Mitigation: Treat token estimates and compression suggestions as advisory, especially when usage data may be incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-zihan/skills/context-budget-analyzer)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis report; optional JSON output from the bundled analysis scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token counts are estimates unless derived from recorded usage data; reports are read-only and redact sensitive strings.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
