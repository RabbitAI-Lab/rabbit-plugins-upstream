## Description: <br>
Sports Inc SportsLink API adapter for retrieving dealer invoice documents, normalizing them for payables workflows, and marking successfully imported documents as consumed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zmtucker](https://clawhub.ai/user/zmtucker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Accounts payable agents and operations teams use this skill to fetch Sports Inc invoice documents, normalize invoice fields for downstream matching, and mark only successfully imported documents historical. It is intended as a source adapter paired with a payables workflow or ERP adapter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a SportsLink API key to access dealer invoice data. <br>
Mitigation: Install it only for agents that should access the dealer's Sports Inc invoices and share SPORTSINC_API_KEY only through the intended credential mechanism. <br>
Risk: Including historical documents can broaden retrieval beyond the active unimported invoice inbox. <br>
Mitigation: Keep include_historical disabled unless historical or consumed documents are explicitly needed. <br>
Risk: mark-historical changes document status and can hide invoices from the active workflow if used too early. <br>
Mitigation: Run mark-historical only after the downstream bill or import succeeds; use SPORTSINC_DRY_RUN when validating the flow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zmtucker/skills/sportsinc-sportslink) <br>
- [Sports Inc homepage](https://www.sportsinc.com) <br>
- [SportsLink API reference](artifact/references/sportslink_api.md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON objects from a Python CLI, with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, requests, and SPORTSINC_API_KEY; SPORTSINC_API_URL and SPORTSINC_DRY_RUN are optional.] <br>

## Skill Version(s): <br>
0.3.2 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
