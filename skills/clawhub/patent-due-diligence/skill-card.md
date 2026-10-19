## Description:

Checks a company's patents, ownership changes, and recorded pledges and licenses before investment, M&A, or partnership, producing a due-diligence checklist and risk summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, M&A teams, and business partners use this skill to review a target company's patent holdings, ownership history, and recorded legal events and identify questions for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential transaction details, company names, or patent queries may be sent to the external PatentMax service.

Mitigation: Use only when sharing these details with PatentMax/ip930.com is acceptable; review before handling confidential M&A, investment, unpublished invention, or trade-secret material.

Risk: The trial flow automatically creates and stores an API credential locally, and a custom service endpoint could receive queries and credentials.

Mitigation: Use PATENTMAX_API_KEY only in a trusted environment, expect a local ~/.patentmax credential/cache directory, and leave PATENTMAX_BASE_URL unset unless the endpoint is trusted.

Risk: Patent database events may lag official records, and unrecorded licenses or agreements may not appear.

Mitigation: Confirm material ownership, pledges, and licenses against official patent registers and underlying contracts before making transaction decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-due-diligence)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax query syntax](artifact/references/query-syntax.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [UTF-8 BOM CSV checklist and conversational risk summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checklist records patent identifiers, legal status, ownership changes, recorded legal events, and potential risks; findings require verification against official records and contracts.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
