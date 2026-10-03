## Description:

euthyna-en guides agents through evidence-based code security audit adjudication, requiring measured facts, file-line evidence, verification gates, and explicit inconclusive outcomes before findings are delivered.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to audit code, pull requests, changes, repositories, or suspected vulnerability claims with evidence gates before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may read local repositories, git history, dependency metadata, and coverage files while preparing a security audit.

Mitigation: Run it only on repositories the user is authorized to inspect, and review planned commands before execution on sensitive codebases.

Risk: Verification or proof-of-concept steps can execute commands on the user's machine and may write audit reports.

Mitigation: Confirm exact commands and output locations before execution, and prefer a sandbox or throwaway environment for reproduction steps.

Risk: Missing measurements can be mistaken for clean results if the process is abbreviated.

Mitigation: Preserve the skill's three-state reporting discipline and mark unavailable measurements as not evaluable instead of clean.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/modusensus/skills/euthyna-en)
- [verification-gates.md](references/verification-gates.md)
- [change-audit.md](references/change-audit.md)
- [dependency-audit.md](references/dependency-audit.md)
- [fact-producers.md](references/fact-producers.md)
- [fact-contract.md](references/fact-contract.md)
- [bug-classes.md](references/bug-classes.md)
- [meta-mechanisms.md](references/meta-mechanisms.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, configuration]

**Output Format:** [Markdown audit reports with structured findings, file-line evidence, reproduce commands, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require report files to be written to disk and checked by a gate command before delivery.]

## Skill Version(s):

0.4.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
