## Description:

Manages project documentation: CLAUDE.md, AGENTS.md, README.md, CONTRIBUTING.md, DOCS.md.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to initialize, verify, and refresh repository context and documentation files against the actual codebase state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify repository documentation files and create CLAUDE.md symlinks during initialize or update workflows.

Mitigation: Use --dry-run for a preview or --preserve for narrower changes, and review resulting diffs before accepting updates.

Risk: Generated or refreshed documentation can become misleading if repository commands, paths, or conventions are not verified.

Mitigation: Follow the skill's verification workflow and check referenced commands and paths against the current codebase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-md-docs)
- [Initialize Context Workflow](references/init-agents.md)
- [Monorepo Handling](references/monorepo.md)
- [Update Context Files Workflow](references/update-agents.md)
- [Update CONTRIBUTING Workflow](references/update-contributing.md)
- [Update README Workflow](references/update-readme.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown files with concise status summaries and optional diffs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify tracked markdown files and create CLAUDE.md symlinks when requested.]

## Skill Version(s):

4.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
