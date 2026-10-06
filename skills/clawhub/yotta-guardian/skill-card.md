## Description:

Evaluates proposed agent tool calls with deterministic rules and optional intent verification, returning risk decisions and audit records before dangerous operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to screen proposed commands and sensitive file operations before execution and retain an audit trail of the decision. It evaluates calls but does not execute them or replace host permissions and human approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installers may write outside the intended skills directory through existing symlinks.

Mitigation: Review before installation; use a trusted, empty skills directory with no symlinks, and avoid untrusted project worktrees or elevated privileges.

Risk: An external intent verifier may receive previews of commands, paths, and content.

Mitigation: Configure an external verifier only when you trust its destination and handling of those previews.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Project homepage (declared)](https://github.com/YottaMeta/yotta-guardian)
- [Rule catalog](artifact/references/rules.md)
- [Policies and exit codes](artifact/references/policies.md)
- [Intent verifier protocol](artifact/references/intent-verifier.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON verdicts, Audit logs]

**Output Format:** [Text or JSON decisions; optional JSONL audit records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports matched rules and risk severity; does not execute proposed operations.]

## Skill Version(s):

0.1.8 (source: server release, frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
