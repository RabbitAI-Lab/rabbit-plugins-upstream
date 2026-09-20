## Description:

A local Chinese-language checker for China ETS emission report tables that performs six deterministic recalculation and consistency checks, cites source line numbers and figures, and returns no conclusion when required input is missing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Energy, environmental, safety, and finance staff at China ETS covered entities use this skill to self-check annual greenhouse-gas emission report tables before third-party verification or resubmission. It recalculates reported emissions and table totals, flags duplicate or inconsistent rows, and lists missing or unrecognized required fields without making unsupported conclusions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users could mistake the checker output for an official verification or regulatory compliance conclusion.

Mitigation: Use it as a pre-verification arithmetic and consistency aid; keep formal compliance, factor-selection, source-truth, and third-party verification decisions with qualified reviewers.

Risk: The free release omits five disclosed checks, including prior-year comparison, official-factor comparison, quota comparison, cross-version inconsistency checks, and facility-by-scope action summaries.

Mitigation: Review the reported executed and withheld checks before relying on results, and do not interpret omitted checks as passed.

Risk: Carbon-emission report tables may contain sensitive operational data even when processing is local.

Mitigation: Run the Node script only in a trusted local environment and install it only if local processing of pasted report data is acceptable for the organization.

Risk: The interface and results are primarily in Chinese, which can lead to misinterpretation by non-Chinese readers.

Mitigation: Have Chinese-literate domain staff review findings, missing-input messages, and withheld-check notices before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/carbon-emission-report-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Chinese human-readable console text or JSON diagnostics from a local Node.js script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers and numeric values; insufficient input returns missing-field guidance and no pass/fail conclusion.]

## Skill Version(s):

1.0.7 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
