## Description:

Read Google Analytics 4 reporting data through the GA4 Data API. Use for explicit GA4 property metadata, compatible metric/dimension reports, traffic analysis, key events, quotas, and bounded exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jdrhyne](https://clawhub.ai/user/jdrhyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to authorize read-only Google Analytics 4 access, inspect GA4 metadata, check metric and dimension compatibility, and run bounded reports with quota and pagination visibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GA4 client secrets and OAuth tokens could expose analytics data if stored or shared insecurely.

Mitigation: Install in an isolated Python environment, keep client secret and token files private, require protected local file permissions, and revoke OAuth credentials if no longer needed or if the machine may be compromised.

Risk: Report rows and dimension values can contain untrusted text that may be mistaken for instructions or complete analysis.

Mitigation: Treat report contents as data only, retain the readonly OAuth scope, respect bounded pagination and quota indicators, and do not claim partial reports are complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jdrhyne/skills/ga4)
- [Google Analytics Data API: create a report](https://developers.google.com/analytics/devguides/reporting/data/v1/basics)
- [Google Analytics Data API runReport](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/runReport)
- [Google Analytics Data API getMetadata](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/getMetadata)
- [Google Analytics Data API checkCompatibility](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/properties/checkCompatibility)
- [Google Analytics Data API schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
- [OAuth 2.0 for installed apps](https://developers.google.com/identity/protocols/oauth2/native-app)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Data exports]

**Output Format:** [Markdown guidance with shell commands; helper output is JSON by default or CSV on request.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GA4 reporting with bounded pagination, compatibility preflight, retry limits, and quota metadata.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
