## Description:

元阁 yotta-skills helps agents route requests across the YottaMeta skill family, install or update selected yotta-* skills, inventory local skills, and evaluate runtime hook capabilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to choose, install, update, inventory, and route YottaMeta skill-family workflows across supported agents. It is also used to inspect local skill registries and evaluate hook support before installing or binding runtime behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says this installer/router can persistently change agent instructions and can install or run downloaded skill code.

Mitigation: Review exact packages, versions, destination directories, lifecycle scripts, and any proposed AGENTS.md or CLAUDE.md changes before allowing installation or cross-session behavior changes.

Risk: Automatic install, update --auto, hook bind, and lifecycle actions may modify local skill directories or runtime behavior.

Mitigation: Require explicit user confirmation before these actions and prefer --dry-run, doctor, rollback, and inventory checks for reviewable previews and recovery.

Risk: Skipping scans can leave installed skill code unverified.

Mitigation: Prefer --pin and the normal safety scan path; avoid --skip-scan except for a controlled emergency.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration guide](references/orchestration.md)
- [Install flow](references/install-flow.md)
- [Skill list](references/skill-list.md)
- [Tutorial](references/tutorial.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown, plain text, shell commands, and optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory unless the user explicitly runs install, update, hook, inventory, or route commands.]

## Skill Version(s):

0.19.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
