## Description:

Checks tender bid materials locally for line-item pricing arithmetic errors and unreplaced template placeholders in the free tier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, bid, and compliance teams use this skill to run a zero-cost pre-submission check on bidder materials for arithmetic mismatches and leftover template placeholders. It is a preliminary review aid and does not replace legal advice or evaluation committee judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender-document checks can be mistaken for legal, scoring, or evaluation committee determinations.

Mitigation: Use the output as a preliminary AI check only; keep formal bid evaluation and legal review in the responsible human workflow.

Risk: Documentation mentions anonymous usage statistics, while the inspected packaged code does not implement outbound material transfer or persistence.

Mitigation: Confirm telemetry expectations with the publisher if usage statistics affect deployment policy, and review the packaged script before use.

Risk: Incomplete or malformed bidder input can produce an insufficient-input result rather than a substantive check.

Mitigation: Provide a bidders array with each bidder's structured items and/or text, and treat insufficient-input results as a request for more material, not as a clean finding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tenderaudit-full-compliance-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON from a local Node.js command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bidder JSON input; returns insufficient-input status instead of conclusions when materials cannot be checked.]

## Skill Version(s):

1.1.39 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
