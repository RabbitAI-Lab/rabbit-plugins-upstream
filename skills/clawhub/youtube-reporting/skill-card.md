## Description: <br>
YouTube Reporting API integration with managed OAuth for scheduling and downloading bulk YouTube Analytics reports as CSV files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manage YouTube Reporting API jobs, list report types, retrieve generated reports, and download daily CSV analytics for connected YouTube channels or playlists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Maton API key and managed OAuth to access YouTube Reporting data for the connected Google account. <br>
Mitigation: Install only when comfortable authorizing Maton to proxy YouTube Reporting API requests, and treat MATON_API_KEY as a secret. <br>
Risk: Requests may target the wrong YouTube account when multiple connections exist. <br>
Mitigation: Verify the intended YouTube connection and use the Maton-Connection header when more than one connection is available. <br>
Risk: Creating or deleting reporting jobs changes the set of reports generated for a channel or playlist. <br>
Mitigation: Confirm the report type and intended effect with the user before creating or deleting a reporting job. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/youtube-reporting) <br>
- [Maton Homepage](https://maton.ai) <br>
- [YouTube Reporting API Overview](https://developers.google.com/youtube/reporting) <br>
- [YouTube Reporting API Reference](https://developers.google.com/youtube/reporting/v1/reference/rest) <br>
- [Bulk Reports](https://developers.google.com/youtube/reporting/v1/reports) <br>
- [Report Types](https://developers.google.com/youtube/reporting/v1/reports/full_report_list) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline Python, JavaScript, shell, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, a valid MATON_API_KEY, and an authorized YouTube Reporting connection.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
