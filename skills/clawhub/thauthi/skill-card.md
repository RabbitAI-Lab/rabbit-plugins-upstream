## Description:

Thauthi gives coding agents Python tools for runtime tracing, exception recovery, behavior checks, AST transformations, recorded I/O replay, code synthesis, and repository-wide call-site updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ntrieuvi97](https://clawhub.ai/user/ntrieuvi97)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Thauthi with coding agents to investigate Python behavior, replay captured I/O, generate or check code changes, and update repository call sites. Commands with --apply can write changes to the repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chronos cassettes record raw intercepted arguments and results without redaction, which may include credentials or personal data.

Mitigation: Avoid running Chronos with production secrets or sensitive environments, ignore .thauthi/cassettes/, and do not commit or upload cassette files.

Risk: Commands using --apply may change repository files.

Mitigation: Review the resulting changes before keeping them.

Risk: The security evidence reports a benign result with medium confidence, but analysis was partial because some local references were unresolved.

Mitigation: Review unresolved references and inspect the skill source before deployment; the scan is not a guarantee of safety.

## Reference(s):

- [Thauthi on ClawHub](https://clawhub.ai/ntrieuvi97/skills/thauthi)
- [Publisher profile: ntrieuvi97](https://clawhub.ai/user/ntrieuvi97)

## Skill Output:

**Output Type(s):** [Analysis, Code, Files, Shell commands, Guidance]

**Output Format:** [CLI commands, diagnostic reports, regression tests, and Python code or repository changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands using --apply can modify files; Chronos cassettes capture unredacted call arguments and return values.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
