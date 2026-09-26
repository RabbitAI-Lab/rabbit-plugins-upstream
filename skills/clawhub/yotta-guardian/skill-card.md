## Description:

Checks proposed agent tool calls for dangerous commands and sensitive file operations, returning rule-based verdicts and an audit trail before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review high-risk tool calls before execution, including destructive shell commands, privilege changes, and writes to sensitive paths. It provides allow, warn, or deny verdicts and audit records; it does not execute the proposed calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Treating an advisory verdict as an operating-system sandbox could leave dangerous actions unguarded.

Mitigation: Run checks before tool execution and retain authorization and execution controls outside the skill.

Risk: Installing from an untrusted source or globally could distribute untrusted skill files across agents.

Mitigation: Install from a trusted source and use the global option only when installation to multiple agents is intended.

Risk: A configured external intent verifier runs a command outside the rule-based check.

Mitigation: Configure only verifier commands you trust.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Project homepage](https://github.com/YottaMeta/yotta-guardian)
- [Rule catalog](references/rules.md)
- [Policies and exit codes](references/policies.md)
- [Intent verifier protocol](references/intent-verifier.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples; machine-readable JSON verdicts when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposed calls are evaluated before execution; verdicts can be audited.]

## Skill Version(s):

0.1.6 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
