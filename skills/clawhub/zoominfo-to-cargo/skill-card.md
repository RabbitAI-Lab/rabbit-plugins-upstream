## Description:

Compares verified contact and company coverage from a ZoomInfo export with Cargo enrichment on a small sample before a renewal decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and sales teams compare verified coverage and sample credit costs before deciding whether to renew a contact-data provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business contact and company data may be sent to Cargo and its enrichment providers.

Mitigation: Review data-sharing permissions and use an approved, limited sample before sending records.

Risk: Optional attribution probes local agent configuration and creates persistent session or marker state unrelated to the comparison.

Mitigation: Review and skip optional attribution or marker steps unless their purpose and local effects are acceptable.

Risk: Optional GitHub starring acts through the user's account, and unpinned follow-on installs can change the local environment.

Mitigation: Do not run these optional commands without explicit user approval; review and pin installation sources first.

Risk: A full-list enrichment run can consume substantially more credits than the sample.

Mitigation: Report sample cost and estimated full-run credits, then obtain approval before scaling.

## Reference(s):

- [Cargo GTM skills](https://github.com/getcargohq/gtm-skills)
- [Cargo waterfall playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/waterfall.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown comparison with verified coverage, credit costs, and example CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a 10–20 record sample before a separately approved full run.]

## Skill Version(s):

1.0.2 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
