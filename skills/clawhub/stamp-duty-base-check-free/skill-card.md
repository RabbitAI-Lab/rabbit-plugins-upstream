## Description:

印花税计税依据台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly or quarterly close, reconciliation, or stamp-duty filing preparation to check a Chinese stamp-duty taxable-base ledger. It recalculates row-level tax, compares declared base against contract amount, checks totals, detects duplicate contract numbers, and flags blank or placeholder fields without making taxability determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The inspected help text mentions anonymous usage statistics and a --no-stats option, but the inspected argument parser does not implement --no-stats.

Mitigation: Review the telemetry wording and CLI behavior before use or publication; do not represent --no-stats as available until the option is implemented or the wording is corrected.

Risk: The checker performs deterministic ledger reconciliation and explicitly does not decide whether a contract is taxable, which tax item applies, or how special tax treatments should be handled.

Mitigation: Use the output as arithmetic and consistency support only, and have qualified tax staff review taxability, rate selection, exemptions, and special cases.

Risk: Materials that are incomplete or missing required ledger columns can produce an insufficient-input result rather than a reconciliation conclusion.

Mitigation: Provide a ledger with the required headers and contract rows, and treat insufficient-input output as a request for more source material rather than as a clean result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/stamp-duty-base-check-free)
- [Skill source documentation](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or structured JSON containing executed checks, missing-input guidance, findings, summary counts, and stated out-of-scope checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library, reads a user-provided ledger file or sample input, and exits with documented status codes for success, missing input, insufficient materials, parse/read errors, or unexpected errors.]

## Skill Version(s):

1.0.51 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
