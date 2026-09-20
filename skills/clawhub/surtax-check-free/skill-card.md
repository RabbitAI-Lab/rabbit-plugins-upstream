## Description:

Checks Chinese VAT surtax worksheets by recalculating city construction tax, education surtax, local education surtax, totals, duplicate periods, and blank fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance and tax operations users can run this local checker against copied VAT surtax worksheet text to identify arithmetic, total-row, duplicate-period, and blank-field issues. It is a mechanical recalculation aid, not tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users could mistake mechanical recalculation results for tax advice or policy validation.

Mitigation: Use the output as a worksheet consistency aid and have qualified tax staff verify applicability, exemptions, and filing decisions.

Risk: The free version intentionally withholds several validation checks, including negative VAT basis and abnormal rate checks.

Mitigation: Review the listed withheld and out-of-scope checks before relying on a clean result, especially for filing or audit workflows.

Risk: Runtime text mentions anonymous stats, while the security evidence says no network reporting is implemented.

Mitigation: Clarify the stats wording with the publisher before use in sensitive environments, and evaluate any future release that adds network behavior.

Risk: Poorly formatted input or missing headers can prevent checks from running.

Mitigation: Provide worksheet text with the required headers and review insufficient-input messages instead of treating them as successful checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/surtax-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or structured JSON findings with source line numbers, executed checks, withheld checks, and summary totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on worksheet text input; the free version reports only its included checks and lists checks that were not run.]

## Skill Version(s):

1.0.29 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
