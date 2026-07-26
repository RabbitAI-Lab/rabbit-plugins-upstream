## Description: <br>
Google Analytics API integration with managed OAuth for managing Admin API resources and running Data API reports through Maton. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rich-song](https://clawhub.ai/user/rich-song) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure Google Analytics OAuth connections, inspect accounts and properties, and query GA4 reporting metrics through Maton-managed API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a Maton API key and Google OAuth connections. <br>
Mitigation: Protect MATON_API_KEY and install the skill only when Maton is the intended OAuth and API gateway. <br>
Risk: Admin API requests can change Google Analytics account, property, data stream, dimension, or conversion settings. <br>
Mitigation: Review account and property identifiers before executing Admin API create, update, or delete requests. <br>
Risk: Deleting a Maton connection can disrupt access for workflows that rely on that connection. <br>
Mitigation: Confirm the connection ID and downstream usage before deleting a connection. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rich-song/skills/google-analytics-api) <br>
- [Google Analytics Admin API overview](https://developers.google.com/analytics/devguides/config/admin/v1) <br>
- [Google Analytics Data API overview](https://developers.google.com/analytics/devguides/reporting/data/v1) <br>
- [Google Analytics Data API runReport method](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, JavaScript, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY, and separate Google Analytics Admin API or Data API connections as needed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
