## Description:

This skill locally checks bank acceptance bill ledgers for maturity-date calculation, receivables balance consistency, duplicate bill numbers, missing status, nonpositive amounts or terms, and settled bills still counted in balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and treasury staff use this skill to check bank acceptance bill ledgers against stated accounting rules before month-end reconciliation. It reports line-referenced findings and withholds conclusions when the input is incomplete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat ledger findings as bank verification or legal advice.

Mitigation: Use the output as accounting assistance only; verify bill authenticity and recourse status with the accepting bank or ECDS and consult qualified advisors when needed.

Risk: Incomplete or malformed ledger input can lead to no conclusion rather than a pass.

Mitigation: Provide a complete table with recognizable headers and review insufficient-input messages before relying on any result.

Risk: The free-tier scope can be misunderstood because some checks are withheld and the documentation has a listed-scope inconsistency.

Mitigation: Review the emitted executed-checks and withheld-checks lists for the actual scope of each run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/bank-acceptance-bill-check-free)
- [Artifact skill definition](artifact/SKILL.md)
- [Sample ledger input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or structured JSON from the local checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and include executed checks, withheld checks, and insufficient-input status when applicable.]

## Skill Version(s):

1.0.59 (source: server evidence release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
