## Description:

Provides an evidence-led adjudication workflow for code security audits and vulnerability claims, using deterministic fact collection, six review gates, and downgrading unsupported claims to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use the skill to assess repositories, code changes, and vulnerability claims through measured evidence and a structured adjudication process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit workflow may lead users to run untrusted project tests, builds, or exploit proofs without adequate safeguards.

Mitigation: Review the skill's execution guidance and establish appropriate safeguards before running untrusted tests, builds, or proofs.

## Reference(s):

- [euthyna (English) on ClawHub](https://clawhub.ai/modusensus/skills/euthyna-en)
- [Bug classes](artifact/references/bug-classes.md)
- [Change audit](artifact/references/change-audit.md)
- [Dependency audit](artifact/references/dependency-audit.md)
- [Fact contract](artifact/references/fact-contract.md)
- [Fact producers](artifact/references/fact-producers.md)
- [Meta mechanisms](artifact/references/meta-mechanisms.md)
- [Verification gates](artifact/references/verification-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Code, Shell commands, Guidance]

**Output Format:** [Markdown audit reports with structured JSON evidence and reproducible commands or proof examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written to disk and distinguish evaluated, flagged, and unevaluable criteria.]

## Skill Version(s):

0.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
