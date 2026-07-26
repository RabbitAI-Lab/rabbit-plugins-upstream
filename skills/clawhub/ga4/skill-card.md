## Description: <br>
GA4 Analytics queries Google Analytics 4 data through the Analytics Data API for page performance, traffic sources, user and session metrics, conversions, date ranges, and filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jdrhyne](https://clawhub.ai/user/jdrhyne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and site operators use this skill to retrieve read-only GA4 reports for common website analytics questions, including top pages, traffic sources, users, sessions, conversions, and filtered date ranges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires sensitive Google OAuth credentials, including a refresh token. <br>
Mitigation: Use a dedicated Google OAuth client where possible, keep tokens out of shared terminals and logs, and store credentials only in the intended environment. <br>
Risk: The configured credentials grant read-only access to the selected GA4 property. <br>
Mitigation: Install only when read-only GA4 access is acceptable and verify that the Google consent screen requests Analytics read-only scope. <br>
Risk: The scripts depend on external Python packages. <br>
Mitigation: Install dependencies from trusted package sources before use. <br>


## Reference(s): <br>
- [ClawHub GA4 Analytics skill page](https://clawhub.ai/jdrhyne/skills/ga4) <br>
- [Google Analytics documentation](https://developers.google.com/analytics) <br>
- [Google Analytics Data API setup](https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with bash examples; script output can be table, JSON, or CSV] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python plus GA4_PROPERTY_ID, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, and GOOGLE_REFRESH_TOKEN environment variables.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
