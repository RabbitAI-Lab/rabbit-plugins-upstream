## Description:

Guides coding agents to understand real repository structure and constraints before making changes, using evidence-driven codebase discovery, architecture mapping, implementation planning, risk calibration, validation, and delivery practices for medium to large software engineering tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liubai00](https://clawhub.ai/user/liubai00)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineering agents use this skill when working in existing software repositories where correct changes depend on understanding project rules, architecture, code paths, build manifests, migrations, tests, workspace state, and risk level. It is intended for repository analysis, scoped implementation, review, validation, and handoff, not for unrelated writing tasks or single-file mechanical edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository inventory output can expose repository paths, branch and head information, structural filenames, and other project context if shared publicly.

Mitigation: Review generated inventory and delivery output before sharing outside the intended audience.

Risk: The skill helps agents inspect project structure and relevant source context, which may include sensitive local or proprietary repository information.

Mitigation: Use it only in repositories where agent inspection is authorized and keep credentials, private data, and production details out of reports and test fixtures.

## Reference(s):

- [Project repository homepage](https://github.com/liubai00/project-engineering)
- [ClawHub skill page](https://clawhub.ai/liubai00/skills/project-engineering)
- [Usage guide](docs/USAGE.md)
- [Architecture guidance](references/architecture.md)
- [Discovery guidance](references/discovery.md)
- [Implementation guidance](references/implementation.md)
- [Risk and archetypes guidance](references/risk-and-archetypes.md)
- [Delivery guidance](references/delivery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline code, shell commands, file references, and validation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repository inventory findings, risk classification, implementation plans, code changes, test commands, and delivery summaries.]

## Skill Version(s):

1.0.0 (source: changelog, released 2026-08-21; server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
