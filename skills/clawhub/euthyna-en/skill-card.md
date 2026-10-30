## Description:

The adjudication discipline and delivery gate for code security audits, grounding conclusions in measured evidence and downgrading unsupported claims to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Use for repository, change, or suspected-vulnerability security audits that need evidence-backed adjudication. The skill gathers deterministic facts, evaluates claims against defined verification gates, and reports unsupported claims as observations rather than confirmed findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification commands and vulnerability demonstrations may have side effects when run against real projects.

Mitigation: Review the separately supplied CLI, approve verification commands individually, and run tests and demonstrations in a disposable environment without personal credentials or production data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Publisher profile](https://clawhub.ai/user/modusensus)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Evidence-backed Markdown audit reports, claim assessments, pseudocode, proof-of-concept demonstrations, and verification commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are tied to evidence; claims that do not meet verification gates are downgraded to observations.]

## Skill Version(s):

0.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
