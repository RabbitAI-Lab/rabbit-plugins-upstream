## Description: <br>
Sports Inc SportsLink API adapter for retrieving dealer invoice documents from SportsLink, normalizing them into a common invoice shape, and marking imported documents consumed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Accounts payable agents and operators use this skill to retrieve Sports Inc invoices, normalize document headers and line items for PO matching, and mark only successfully imported documents as consumed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access API-key-scoped Sports Inc invoice data. <br>
Mitigation: Install only for agents that should access Sports Inc invoices and share SPORTSINC_API_KEY only with intended delegation connections. <br>
Risk: customer_ref is advisory and does not limit which invoices the SportsLink API returns. <br>
Mitigation: Treat the SportsLink API key as the effective data scope and rely on downstream payables workflows for customer-specific matching. <br>
Risk: mark-historical changes document status in SportsLink. <br>
Mitigation: Use dry-run or human review when appropriate and mark documents historical only after the payable has been created successfully. <br>
Risk: Scanned or OCR documents may lack line-item detail. <br>
Mitigation: Prefer EDI documents for line verification and escalate header-only documents instead of billing them blindly. <br>


## Reference(s): <br>
- [SportsLink API Reference](references/sportslink_api.md) <br>
- [Sports Inc](https://www.sportsinc.com) <br>
- [SportsLink API](https://api.sportsinc.com/) <br>
- [ClawHub Skill Page](https://clawhub.ai/zmtucker/skills/sportsinc-sportslink) <br>
- [Publisher Profile](https://clawhub.ai/user/zmtucker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses for helper actions and compact Markdown summaries for delegated tasks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SPORTSINC_API_KEY; list and get actions read invoice documents, while mark-historical changes document status after successful import.] <br>

## Skill Version(s): <br>
0.4.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
