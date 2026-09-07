## Description:

Turn photos of offline posters, signboards, flyers, and billboards into a traceable business-lead pipeline that extracts visible details, researches public business contacts and decision-makers with bounded TreeBased search, and prepares Notion dashboard records and outreach drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiwithenoch](https://clawhub.ai/user/aiwithenoch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and sales or marketing operators use this skill to convert photos of offline business advertising into researched lead records, public contact paths, Notion-ready dashboards, and reviewed outreach drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Noisy or incomplete images and public web sources can lead to incorrect or unverified lead details.

Mitigation: Keep raw and normalized values side by side, cite material findings, label confidence, and leave ambiguous fields unresolved for review.

Risk: Notion dashboard updates can write to an external lead database.

Mitigation: Require a clear destination, preview creates and updates, upsert by stable identity keys, and preserve manual notes and corrected values.

Risk: Outreach can contact unsuitable recipients if messages are sent without final review.

Mitigation: Send only after explicit approval of the exact batch, use public business or professional contact paths, include opt-out language, and skip private, guessed, contradictory, or Do not contact leads.

Risk: Business lead research can drift into private-person discovery or data-broker enrichment.

Mitigation: Use only public business information and public professional contact paths; avoid data brokers, leaked datasets, private accounts, personal home addresses, and guessed emails.

## Reference(s):

- [TreeBased Search](references/treebased-search.md)
- [Notion Dashboard](references/notion-dashboard.md)
- [Outreach](references/outreach.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown summaries and lead tables, with optional CSV, JSON, or Notion database records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, confidence labels, dashboard status, outreach approval state, and unresolved questions when evidence is incomplete.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
