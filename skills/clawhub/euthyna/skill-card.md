## Description:

Euthyna guides code security audits by grounding findings in deterministic evidence, applying six verification gates, and downgrading unsupported claims to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use Euthyna to audit repositories, pull requests, and suspected vulnerability claims. It helps verify findings with measured evidence and record unsupported or unassessed claims honestly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification commands and exploit tests can affect the audited environment, and reports may contain sensitive information.

Mitigation: Review commands before execution, obtain explicit approval for verification or PoC runs, use an isolated environment where possible, and handle saved reports carefully.

Risk: The security scan was partial because several referenced paths were missing, so its evidence does not cover the complete picture.

Mitigation: Treat the scan as incomplete, identify missing paths, and record uncovered checks as unassessed rather than clean.

## Reference(s):

- [Euthyna on ClawHub](https://clawhub.ai/modusensus/skills/euthyna)
- [Bug Classes](references/bug-classes.md)
- [Change Audit](references/change-audit.md)
- [Dependency Audit](references/dependency-audit.md)
- [Fact Contract](references/fact-contract.md)
- [Fact Producers](references/fact-producers.md)
- [Meta Mechanisms](references/meta-mechanisms.md)
- [Verification Gates](references/verification-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit reports with evidence, findings, reproduction commands, and gate status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Unsupported findings are downgraded to observations; incomplete assessments can be marked inconclusive.]

## Skill Version(s):

0.11.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
