## Description:

Helps teams build B2B lead and account lists, enrich and verify professional contacts, score prospects, prepare outreach, sync CRM data, and monitor buying signals with Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and revenue operations teams use this skill to source target companies and contacts, research and enrich business data, verify leads, score fit, prepare personalized outreach, update CRM records, and track account signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some instructions may permit campaign launches or LinkedIn actions beyond the stated draft-only boundary.

Mitigation: Resolve the draft-only boundary and require explicit approval of the account, recipients, and message before external actions.

Risk: Newly found contacts could be enriched before suppression checks, or CRM data could be sent to providers without approval.

Mitigation: Check contacts against suppression records before enrichment and approve which CRM fields may be shared with providers.

Risk: Unreviewed dependencies or recurring workflows may introduce unexpected behavior.

Mitigation: Pin reviewed dependencies and explicitly approve recurring workflows.

## Reference(s):

- [Cargo GTM skill guide](artifact/SKILL.md)
- [Acceptable use](artifact/references/acceptable-use.md)
- [Contact accuracy](artifact/references/contact-accuracy.md)
- [Cost discipline](artifact/references/cost-discipline.md)
- [Finding companies and contacts](artifact/guides/finding-companies-and-contacts.md)
- [Enriching and researching](artifact/guides/enriching-and-researching.md)
- [Writing outreach](artifact/guides/writing-outreach.md)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/cargo-gtm)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, CRM updates]

**Output Format:** [Lead and account research, prospect tables, scores, outreach drafts, and Cargo CLI JSON results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected data providers, account permissions, and the user's Cargo workspace.]

## Skill Version(s):

2.8.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
