## Description:

Answers questions about website traffic from Google Analytics 4 using read-only Google Analytics API calls and returns report rows to the agent conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, site owners, and support agents use this skill to answer GA4 traffic, realtime, comparison, ecommerce, and setup questions without manually working through the Google Analytics interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses sensitive Google Analytics credentials to obtain read-only access to selected GA4 properties.

Mitigation: Use a dedicated service account with Viewer access only on required properties, store the key as a protected file path instead of pasted JSON, and rotate or revoke the key when access is no longer needed.

Risk: Analytics report rows returned by the skill enter the agent and model conversation.

Mitigation: Keep redaction and user-dimension blocking enabled, use a GA4 property allowlist when appropriate, and avoid requesting unnecessary sensitive dimensions.

Risk: Every report command makes outbound HTTPS requests to Google OAuth, Analytics Data, and Analytics Admin endpoints.

Mitigation: Install only when that network access is acceptable, and use the documented read-only Analytics scope and destination allowlist behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anatoli-iliev/skills/open-ga4)
- [Publisher profile](https://clawhub.ai/user/anatoli-iliev)
- [Open GA4 repository](https://github.com/anatoli-iliev/open-ga4)
- [README.md](README.md)
- [SETUP.md](SETUP.md)
- [SECURITY.md](SECURITY.md)
- [PRIVACY.md](PRIVACY.md)
- [Google Analytics](https://analytics.google.com/analytics/web/)
- [Google Cloud service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
- [Google Analytics Data API](https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com)
- [Google Analytics Admin API](https://console.cloud.google.com/apis/library/analyticsadmin.googleapis.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance, API calls]

**Output Format:** [Concise text and Markdown tables, with optional JSON output for calculation or setup workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Google Analytics results; dimension-value redaction is enabled by default unless explicitly disabled.]

## Skill Version(s):

0.2.0 (source: frontmatter, package.json, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
