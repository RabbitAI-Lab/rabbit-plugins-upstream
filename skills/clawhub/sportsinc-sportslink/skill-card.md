## Description:

Sports Inc SportsLink API adapter that retrieves dealer invoice documents from SportsWeb, normalizes invoice line and charge data, recovers scanned invoice lines through PDF/OCR review, and marks documents consumed after import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zmtucker](https://clawhub.ai/user/zmtucker)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and payables agents use this skill to pull Sports Inc invoice documents, recover line detail for scanned documents, and hand normalized invoice data to a payables matching workflow. It is intended for controlled Sports Inc dealer payables environments with configured API and portal credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles SportsLink API keys, SportsWeb portal credentials, and optional persisted browser sessions.

Mitigation: Use least-privilege dealer credentials, keep saved session state in a protected secret location, and rotate or delete saved sessions after use.

Risk: The skill can mark invoice documents consumed, which could hide an invoice before billing if used incorrectly.

Mitigation: Enable SPORTSINC_DRY_RUN during testing and mark documents historical only after the downstream bill has been created and verified.

Risk: SportsWeb browser automation may be sensitive to portal policy, MFA, device verification, or environment changes.

Mitigation: Confirm the portal owner permits this automation, test it in a controlled dealer environment, and use manual PDF retrieval when automation is blocked.

Risk: OCR or manual extraction of scanned invoice lines can misread quantities, prices, or document identity.

Mitigation: Reconcile extracted lines against the SportsLink header totals, inspect image pages when OCR confidence or variance is concerning, and escalate any needs_review result.

## Reference(s):

- [SportsLink API reference](references/sportslink_api.md)
- [SportsWeb portal invoice PDF flow](references/sportsweb_flow_notes.md)
- [Reading a Sports Inc invoice PDF](references/pdf_extraction.md)
- [Sports Inc homepage](https://www.sportsinc.com)
- [SportsLink API base URL](https://api.sportsinc.com/)
- [SportsWeb home](https://swv3.sportsinc.com/home)
- [SportsWeb Invoice Center](https://swv2h.sportsinc.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON command responses, compact Markdown summaries, and Markdown with inline bash commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local PDF and image paths for scanned invoice review; requires Sports Inc API and optional SportsWeb portal credential environment variables.]

## Skill Version(s):

0.7.1 (source: artifact/SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
