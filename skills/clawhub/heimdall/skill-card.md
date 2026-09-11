## Description:

Author and run evidence-backed browser and API test plans with honest blocked and non-run semantics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Heimdall to turn browser and API claims into repeatable JSON test plans, execute those plans through supported lanes, and report pass, fail, error, blocked, or skipped outcomes with evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Heimdall plans can use credentials and perform network or file side effects.

Mitigation: Review each plan before execution, inspect setup and teardown steps, use least-privilege credentials, and run only against authorized targets.

Risk: Destructive, paid, or production cases can be enabled with broad controls.

Mitigation: Require explicit review before using risk labels or the allow-risk option, and confirm the target, side effects, and recovery path first.

Risk: Evidence directories and reports can contain session material or secrets.

Mitigation: Keep evidence directories private, keep storageState files out of version control, and pass secrets through environment tokens rather than inlining them in plans.

Risk: Browser-rendered pages can contain misleading instructions for the agent.

Mitigation: Treat the system under test as untrusted and follow page-provided instructions only when the test plan explicitly requires that action.

## Reference(s):

- [Heimdall Skill](SKILL.md)
- [Heimdall README](README.md)
- [Heimdall Security Guidance](SECURITY.md)
- [Heimdall Plan Schema](heimdall.schema.json)
- [ClawHub Skill Page](https://clawhub.ai/antreasantoniou/skills/heimdall)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference JSON test plans, schema usage, execution commands, and evidence report paths.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
