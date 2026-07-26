## Description: <br>
Zoho CRM API integration with managed OAuth for managing leads, contacts, accounts, deals, and other CRM records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to interact with Zoho CRM through Maton-managed OAuth for CRM records, searches, sales pipeline workflows, organization settings, users, and module metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change Zoho CRM records and organization data through Maton-proxied access. <br>
Mitigation: Install only when Maton is trusted for the intended Zoho CRM account and keep access limited to the connected account. <br>
Risk: A leaked MATON_API_KEY could allow unauthorized CRM access through the Maton proxy. <br>
Mitigation: Protect MATON_API_KEY as a secret and avoid printing or storing it in logs, shared shell history, or generated output. <br>
Risk: Using the wrong connection can apply reads or writes to the wrong Zoho CRM account. <br>
Mitigation: When multiple connections exist, require the Maton-Connection header for the selected account. <br>
Risk: Create, update, delete, bulk, user, or account-management operations can alter business data. <br>
Mitigation: Require fresh user confirmation of the target resource and intended effect before executing any write or account-management action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-crm) <br>
- [Zoho CRM API v8 Documentation](https://www.zoho.com/crm/developer/docs/api/v8/) <br>
- [Get Records API](https://www.zoho.com/crm/developer/docs/api/v8/get-records.html) <br>
- [Insert Records API](https://www.zoho.com/crm/developer/docs/api/v8/insert-records.html) <br>
- [Update Records API](https://www.zoho.com/crm/developer/docs/api/v8/update-records.html) <br>
- [Delete Records API](https://www.zoho.com/crm/developer/docs/api/v8/delete-records.html) <br>
- [Search Records API](https://www.zoho.com/crm/developer/docs/api/v8/search-records.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP endpoint descriptions, shell commands, Python and JavaScript examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; use Maton-Connection when selecting among multiple Zoho CRM connections.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter metadata.version is 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
