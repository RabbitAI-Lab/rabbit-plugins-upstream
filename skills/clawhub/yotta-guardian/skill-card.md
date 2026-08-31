## Description:

Yuandun (yotta-guardian) is a cross-agent safety gate that evaluates exec, write, edit, read, run, and shell tool calls with deterministic rules and optional intent verification, returning allow/deny decisions with matched rules and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill as a pre-execution gate before agents run high-risk commands, write sensitive system paths, or change system configuration. It helps surface deterministic allow/deny verdicts and audit trails without executing the operation itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External verifier integrations may share command text, paths, working directory, findings, and short content previews with the configured verifier.

Mitigation: Use external verifiers only when the verifier command or gateway is trusted and appropriate for the data being checked.

Risk: Audit and report outputs may persist safety findings and call details to files.

Mitigation: Enable audit or report output intentionally and store generated logs according to the operator's retention and access-control requirements.

Risk: The skill is a safety checker and does not replace human authorization for high-impact operations.

Mitigation: Treat deny or review verdicts as a stop-and-explain signal, and require explicit operator approval before using configured allow rules for risky maintenance actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Rules Reference](artifact/references/rules.md)
- [Policy and Exit Codes](artifact/references/policies.md)
- [Intent Verifier Protocol](artifact/references/intent-verifier.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-guardian)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, JSON, and Markdown reports with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional JSONL audit logs; optional external verifier requests can include command text, paths, working directory, findings, and short content previews.]

## Skill Version(s):

0.1.2 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
