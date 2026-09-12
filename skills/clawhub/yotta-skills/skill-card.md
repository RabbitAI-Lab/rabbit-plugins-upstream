## Description:

元阁 yotta-skills routes tasks across the YottaMeta skill family, inventories installed skills, and installs or updates selected yotta-* skills through CLI or optional MCP workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External developers and AI agent operators use this skill to decide which YottaMeta skills to combine for a task, inspect local skill inventory, and install or update the YottaMeta skill family into supported agent skill directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can attempt to persist future agent behavior by writing guidance into permanent agent memory files.

Mitigation: Allow permanent-memory writes only when the user explicitly wants cross-session behavior, and review the exact text before accepting it.

Risk: The installer and auto-update flows can place new skills and run verifier code in the user's context.

Mitigation: Review before installing, prefer exact-version installs with --pin, and use a trusted npm registry.

Risk: Unpinned npx or automatic update behavior can fetch newer package contents than originally reviewed.

Mitigation: Avoid unpinned npx in automation and treat update --auto or verifier bootstrap behavior as high-impact.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [README](README.md)
- [Install Flow](references/install-flow.md)
- [Orchestration](references/orchestration.md)
- [Skill List](references/skill-list.md)
- [FAQ](references/faq.md)
- [Walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown or plain text with inline shell commands; JSON when machine-readable CLI or MCP output is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include route confidence, installation status, missing-skill suggestions, registry inventory, and update summaries.]

## Skill Version(s):

0.8.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
