## Description:

Utility Tier Billing Check (Free) is a local Node-based checker that recalculates time-of-use electricity billing worksheets, verifies payable totals, detects duplicate or missing key fields, and cites source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External finance, operations, and facilities users can use this skill to check copied or JSON-formatted utility billing worksheets for arithmetic and table-consistency errors. It is intended for local review of time-of-use electricity bills, with each finding tied back to the input line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation inconsistently mentions anonymous usage statistics, while the inspected code does not implement networking.

Mitigation: Review the release before deployment and treat it as a local Node-based billing checker; provide only the worksheet text or JSON intended for checking.

Risk: The skill checks arithmetic and table consistency, but it does not validate tariff schedules, meter readings, contract changes, or other out-of-scope billing facts.

Mitigation: Use the findings as worksheet-level checks and independently verify tariffs, meter data, and contractual assumptions before relying on billing decisions.

Risk: The release is Chinese-language and domain-specific, which may make review harder for teams without utility-billing or Chinese-language expertise.

Mitigation: Have qualified reviewers confirm the input format, output findings, and billing assumptions before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/utility-tier-billing-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Human-readable console text or JSON result objects with findings, summaries, and cited line numbers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against one provided worksheet text or JSON input; spreadsheet files must be exported or copied to text first.]

## Skill Version(s):

1.0.28 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
