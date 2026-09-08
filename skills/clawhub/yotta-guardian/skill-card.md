## Description:

Yuandun (元盾) is a cross-agent tool-call guardrail that evaluates exec, write, edit, read, run, and shell calls with deterministic rules and optional intent verification, returning allow or deny decisions, matched rules, and audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill as a pre-execution safety gate before an agent runs high-risk commands, writes sensitive system paths, or changes system configuration. It helps surface deterministic allow or deny decisions, matched safety rules, and audit records before irreversible operations occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad installation may enable the skill across more agents than intended.

Mitigation: Install with a specific target such as --agent or --dir unless broad global installation is intended.

Risk: External verifier integrations may receive command and content previews.

Mitigation: Configure external verifiers only when the verifier command or service is trusted to process those previews.

Risk: Audit and report files can persist operational details on disk.

Mitigation: Write audit and report files only to controlled locations and manage retention according to the deployment environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [Rules Reference](references/rules.md)
- [Policies and Exit Codes](references/policies.md)
- [Intent Verifier Protocol](references/intent-verifier.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text safety verdicts, JSON results, Markdown reports, and JSONL audit logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only evaluation by default; optional audit logs and reports may be written when requested.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence; packaged source files report 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
