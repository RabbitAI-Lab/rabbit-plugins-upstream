## Description:

Read supplier terms and create purchase draft records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement operations employees use this skill to prepare supplier purchasing terms from supplied supplier data and, when explicitly requested, create purchase draft records from those terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The create_purchase_draft stage can create a downstream business draft record.

Mitigation: Use the stage only after the user clearly requests draft creation, and review supplier terms before creating the draft.

Risk: Procurement terms may be incorrect if the supplied supplier data is incomplete or inaccurate.

Mitigation: Confirm supplier_id, currency, lead_days, incoterm, and renewal_month before relying on the prepared terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/procurement-draft-desk)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [JSON-compatible structured objects with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces purchase_terms or purchase_draft_id for the current procurement request.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
