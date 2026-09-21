## Description:

元盾 yotta-guardian is a cross-agent guardrail that evaluates exec, write, edit, read, run, and shell tool calls with deterministic rules and optional intent verification, returning allow or deny decisions with matched rules and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent builders use this skill as a pre-execution safety check before an agent runs high-risk commands, writes sensitive paths, or changes system configuration. It helps produce explainable guardrail decisions and audit records for risky tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports that dangerous compound commands may be wrongly allowed.

Mitigation: Review before installing as an automatic guardrail, test compound command handling in the target environment, and do not rely on the skill as the only shell-execution control until the issue is fixed or tightly configured.

Risk: Allowlist overrides and policy choices can reduce blocking behavior for high-risk operations.

Mitigation: Restrict allow and allow-path patterns to explicit authorized maintenance cases, retain audit logging, and require human review for denied or high-impact operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Project homepage](https://github.com/YottaMeta/yotta-guardian)
- [NPM package](https://www.npmjs.com/package/@yottameta/yotta-guardian)
- [Rules reference](references/rules.md)
- [Policies and exit codes](references/policies.md)
- [Intent verifier protocol](references/intent-verifier.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, Markdown reports, shell command examples, and JSONL audit records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces allow, deny, review, severity, matched rule IDs, reasons, exit codes, and optional audit-log entries.]

## Skill Version(s):

0.1.5 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
