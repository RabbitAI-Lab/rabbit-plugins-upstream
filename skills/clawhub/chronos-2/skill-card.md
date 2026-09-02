## Description:

Gives AI coding agents temporal awareness via a hook-backed ledger and decision rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use Chronos to help coding agents make time-aware decisions about retries, stale context, progress reporting, idle loops, and date or recency questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chronos hooks can run automatically in future agent sessions after installation.

Mitigation: Review the hook commands before installing and prefer project-scoped installation when testing.

Risk: The local Chronos ledger records tool timing metadata until retention cleanup removes it.

Mitigation: Treat ledger contents as local operational metadata and avoid sharing them unless needed for debugging or review.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/OthmanAdi/chronos)
- [Chronos homepage](https://aware-bloom-szmt.here.now)
- [Your LLM Agents are Temporally Blind](https://arxiv.org/abs/2510.23853)
- [Chronos npm package](https://www.npmjs.com/package/chronos-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSONL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install local agent hooks that write session timing metadata to a local ledger.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact SKILL.md, CHANGELOG.md, and package.json report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
