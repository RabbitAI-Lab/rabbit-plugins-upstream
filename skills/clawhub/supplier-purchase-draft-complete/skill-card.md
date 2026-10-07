## Description:

Prepares supplier purchasing terms, creates a local purchase draft, and optionally delivers the draft to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams use this skill to turn supplier terms into a purchase draft, retain a local record, and optionally submit the draft to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can submit procurement data externally without a separate confirmation or strict endpoint boundary.

Mitigation: Keep delivery endpoints and credentials unset for local-only use; when delivery is intended, approve a tightly controlled endpoint and use a least-privilege API key.

Risk: The workflow writes a local purchase draft containing supplier terms.

Mitigation: Run it with a dedicated output directory and review the draft before sharing it.

## Reference(s):

- [Supplier Terms Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/supplier-purchase-draft-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local SQLite purchase draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns purchasing terms, draft details, a local record receipt, and a delivery receipt when applicable.]

## Skill Version(s):

1.2.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
