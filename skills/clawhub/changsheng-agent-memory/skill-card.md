## Description:

Cross-session memory recovery for AI agents — your agent never cold-starts again.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ccy123abcd](https://clawhub.ai/user/ccy123abcd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ChangSheng to restore relevant identity, rules, todos, and recent work at session start, track changed files, and hand ongoing work to a fresh session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing may include paths that were not intended.

Mitigation: Preview discovered paths with --list and select the intended files before indexing.

Risk: Memory cleanup may remove useful records.

Mitigation: Review cleanup deliberately and retain backups.

Risk: The optional keyword gate fails open and may not block every unsafe action.

Mitigation: Enable startup instructions or hooks only if wanted, and keep host permissions and approval controls in place.

## Reference(s):

- [Memory system design](references/memory-system.md)
- [ChangSheng on ClawHub](https://clawhub.ai/ccy123abcd/skills/changsheng-agent-memory)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance, shell commands, and local Markdown/JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, file-based outputs; no remote service required.]

## Skill Version(s):

0.99.0 (source: frontmatter, CHANGELOG.md, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
