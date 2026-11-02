## Description:

Evaluates agent tool calls for risky commands and sensitive writes, returning rule-based verdicts and audit records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use the skill to assess agent tool calls before high-risk commands, sensitive-path writes, or system configuration changes, and to retain an audit trail. Treat its verdicts as decision support and keep host permissions and human review in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This release can incorrectly classify destructive commands as safe, so its verdict should not be the sole safeguard.

Mitigation: Preserve host permissions and human approval until the reported parsing, verifier-failure, and exit-code bypasses are corrected.

Risk: Installer changes can affect the selected skill installation target.

Mitigation: Preview one installation target with --dry-run and pin the reviewed version.

Risk: Audit logs and external intent verification may expose sensitive command or path data.

Mitigation: Protect command logs and review sensitive data before enabling external verification.

Risk: Separately fetched packages, verifier programs, and host adapters are outside this security review.

Mitigation: Review those components separately before relying on an integrated deployment.

## Reference(s):

- [Rule reference](references/rules.md)
- [Policy and exit-code reference](references/policies.md)
- [Intent verifier protocol](references/intent-verifier.md)
- [Project homepage listed in package metadata](https://github.com/YottaMeta/yotta-guardian)
- [ClawHub release page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-guardian)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Shell commands, Audit records]

**Output Format:** [Text or JSON verdicts with matched-rule details; optional JSONL audit records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Assesses supplied tool-call data; does not execute the proposed action.]

## Skill Version(s):

0.1.9 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
