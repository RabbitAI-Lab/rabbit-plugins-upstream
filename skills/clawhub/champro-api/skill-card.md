## Description:

CHAMPRO API helps agents use CHAMPRO REST and Custom Builder workflows for inventory, order validation and placement, order status, tracking, warehouse routing, lead-time lookup, and design-to-order flows that are outside CHAMPRO's PromoStandards coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and purchasing operators use this skill to source CHAMPRO stock or custom apparel, validate orders before submission, place sandbox or production orders, and track resulting suborders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place real CHAMPRO orders and partial submissions may create suborders that should not be retried blindly.

Mitigation: Use sandbox first, require human approval for production orders, and escalate partial order results instead of resubmitting the original request.

Risk: Validation bypasses can reduce protection before sending orders.

Mitigation: Keep local validation enabled for normal use and allow skip_validation only under a separate operator policy.

Risk: Order previews, design data, and proof files can contain sensitive customer or team details.

Mitigation: Redact previews before sharing them in tickets and write downloaded proofs only to private intended paths.

## Reference(s):

- [CHAMPRO Development Tools](https://devtools.champrosports.com/#devtools)
- [CHAMPRO Account & Contact Info](https://champrosports.com/AccountAndContactInfo)
- [CHAMPRO API reference](references/api_reference.md)
- [CHAMPRO Custom Builder](references/custom_builder.md)
- [End-to-end flows](references/examples.md)
- [PromoStandards gaps](references/promostandards_gaps.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with JSON CLI inputs and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands read JSON from stdin and produce one JSON object on stdout; proof download actions can write files to an operator-selected local path.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
