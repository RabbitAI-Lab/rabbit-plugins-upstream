## Description:

Helps agents review potentially dangerous tool calls using configurable rules and optional intent checks, returning verdicts and audit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review risky commands and sensitive file operations before execution and retain an audit trail. It is an advisory check, not a substitute for host permissions or human authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker can miss some dangerous commands.

Mitigation: Use it only as an advisory check; retain host permission prompts and human review for destructive operations.

Risk: An external verifier denial can be reported as success.

Mitigation: Do not treat exit code 0 alone as authorization; require normal host approval before executing risky actions.

Risk: Broad installation may expose more agents to an unreliable safety gate.

Mitigation: Install only for the intended agents and review their hook and permission behavior.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Project homepage](https://github.com/YottaMeta/yotta-guardian)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-guardian)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text or JSON verdicts with matched rules and optional audit logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report allow, warn, or deny outcomes; results require independent authorization.]

## Skill Version(s):

0.1.7 (source: server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
