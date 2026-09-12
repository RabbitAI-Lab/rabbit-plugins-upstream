## Description:

Travel-Rule Check is a zero-dependency CLI skill that checks VASP transfer data for originator and beneficiary KYC fields and flags missing information against a USD 1,000 threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, compliance teams, and agent builders use this skill to run lightweight checks on on-chain asset or VASP transfer payloads before higher-risk compliance workflows proceed. It supports self-checks, AI system integration, and regulatory response preparation, but does not replace official requirements or professional legal review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive KYC transaction data is accepted through command-line arguments.

Mitigation: Use synthetic data with the current --tx interface, or adapt the tool to read real KYC data from stdin or a protected file.

Risk: Malformed amounts can be treated as compliant.

Mitigation: Do not rely on the skill as a sole compliance gate until amount validation rejects NaN, infinity, negative, missing, and non-currency values.

Risk: The documented npx global install path is unpinned.

Mitigation: Verify the installer package and source revision before using the global install command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/travel-rule-check)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [CLI text output or JSON result with compliance status, missing fields, and exit code guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic zero-dependency Python CLI output with exit codes 0, 1, and 2.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
