## Description:

Checks Chinese construction progress payment worksheets by recalculating payment, retention, paid amount, totals, duplicate rows, and blank fields, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Construction and finance teams use this skill to check monthly progress payment worksheets for arithmetic mismatches, total-row errors, duplicate contract sections, and missing required cells. The output is arithmetic assistance only and does not provide legal, cost-estimating, contract, or site-completion advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Results may be mistaken for a full construction-payment review even though the free version omits higher-risk checks such as over-contract, inverted cumulative values, out-of-range payment rates, out-of-range retention rates, and negative paid amounts.

Mitigation: Treat results as arithmetic assistance for the executed checks only, review the listed withheld checks, and perform contract or cost-review steps separately when those risks matter.

Risk: The tool does not provide legal, cost-estimating, contract, or physical completion judgments.

Mitigation: Have qualified reviewers verify contract interpretation, site completion, retention rules, and any legal or commercial conclusions outside the worksheet arithmetic.

Risk: Documentation mentions anonymous usage statistics, while the security evidence notes no network or statistics code was present in the inspected package.

Mitigation: Review release notes and inspected code for the installed version before deploying in environments with strict telemetry or network policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/progress-payment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings with source-line references and command-line usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; input must be a JSON or plain-text worksheet containing recognizable table headers.]

## Skill Version(s):

1.0.31 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
