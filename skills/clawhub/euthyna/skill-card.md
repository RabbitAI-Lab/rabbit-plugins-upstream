## Description:

Provides evidence-based guardrails for code security audits, validating findings against deterministic facts and downgrading unsupported claims to observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modusensus](https://clawhub.ai/user/modusensus)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security reviewers use Euthyna to assess code, changes, and suspected vulnerabilities with evidence-based checks. It structures findings into confirmed, rejected, or inconclusive outcomes and guides the creation of an auditable Markdown report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tests, reproduction commands, or proof-of-concept steps may affect the audited repository or expose sensitive credentials.

Mitigation: Approve the exact commands before execution and use a disposable environment without sensitive credentials for unfamiliar repositories.

Risk: The separately obtained CLI and its design documents were not reviewed with this skill release.

Mitigation: Review the CLI separately before use.

Risk: Audit reports may contain sensitive repository details, and temporary or desktop storage can have different access and retention settings.

Mitigation: Choose a private report location with appropriate access and retention.

## Reference(s):

- [Change audit guidance](artifact/references/change-audit.md)
- [Dependency audit guidance](artifact/references/dependency-audit.md)
- [Verification gates](artifact/references/verification-gates.md)
- [Fact contract](artifact/references/fact-contract.md)
- [Fact producer guide](artifact/references/fact-producers.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands]

**Output Format:** [Markdown audit reports with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked findings are classified as confirmed, rejected, or inconclusive.]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
