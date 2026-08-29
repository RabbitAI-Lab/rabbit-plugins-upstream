## Description:

Enforces validation and evidence before claiming work complete, for use before declaring implementation done, creating a PR, or submitting deliverables for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to define acceptance criteria, run validation, capture evidence logs, and avoid premature completion claims before handing off implementation, review, configuration, or deployment work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may treat example command snippets as blanket permission to install packages, start services, or change local environments.

Mitigation: Require user approval for package installs and service starts, and prefer dry runs or isolated local test environments for validation.

Risk: Evidence logs may capture secrets, account details, or sensitive local configuration when commands and outputs are recorded.

Mitigation: Redact secrets and account details before storing or sharing captured evidence.

Risk: Proof-of-work routines can create misleading confidence if checks are performed mechanically or against stale assumptions.

Mitigation: Pair command output with acceptance criteria, version checks, known-issue review, and clear blocker reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-proof-of-work)
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)
- [Atlassian Agile Definition of Done](https://www.atlassian.com/agile/project-management/definition-of-done)
- [Cargo cult programming](https://en.wikipedia.org/wiki/Cargo_cult_programming)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets, checklists, and evidence logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence should cite commands, outputs, timestamps, acceptance criteria, and known blockers when applicable.]

## Skill Version(s):

1.9.19 (source: server release; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
