## Description:

Checks utility tier billing worksheets for arithmetic consistency, row and total reconciliation, duplicate billing items, and missing key fields, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business, finance, and operations users can use this skill to check copied utility billing tables for calculation mismatches, missing required fields, duplicate billing items, and total-row inconsistencies. It is intended for local review of provided billing worksheet text rather than validating meter readings, tariff schedules, or regional electricity policy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is flagged suspicious because its documentation and output direct users toward unpinned payment software and a paid companion skill.

Mitigation: Ignore paid-upgrade prompts unless you separately verify the payment package, exact version, merchant, product, and installed skill contents.

Risk: The checker only covers the free local checks and withholds several negative-value and unit-price range checks.

Mitigation: Use the output as a worksheet arithmetic review only, and do not treat a clean result as validation of tariff rules, meter readings, or checks the artifact lists as not run.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/utility-tier-billing-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Console text or JSON with line-cited findings, summaries, executed checks, withheld checks, and insufficient-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against user-provided utility billing table text; sample input is provided as JSON.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
