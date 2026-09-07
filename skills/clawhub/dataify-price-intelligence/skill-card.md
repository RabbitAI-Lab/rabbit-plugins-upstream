## Description:

Compares product or service prices across sellers, marketplaces, or official pricing pages and produces normalized, evidence-backed pricing findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to collect current pricing evidence, normalize comparable offers, and support price monitoring, offer comparison, channel pricing, or pricing-change decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Dataify token may be exposed through task-monitoring request URLs or copied command output.

Mitigation: Use a dedicated, revocable Dataify token, keep request URLs and logs private, and rotate the token if exposure is suspected.

Risk: The bundle includes Amazon review-scraping behavior beyond price comparison.

Mitigation: Review bundled dependencies before installation and use the review-scraping behavior only when it is explicitly needed and compliant with the target site's terms and applicable policy.

Risk: Generated curl previews or shell commands may be unsafe when populated with untrusted input.

Mitigation: Inspect generated commands before execution and avoid pasting untrusted product names, URLs, or file names into shell commands without proper quoting.

## Reference(s):

- [Dataify Price Intelligence on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-price-intelligence)
- [Dataify Token Setup](_dependencies/skills/dataify-task-operations/references/token-setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration guidance]

**Output Format:** [Markdown reports and JSON result/evidence files with occasional shell commands for setup or resume]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May retain raw responses, hashes, state, and Markdown/JSON reports in the selected output directory.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
