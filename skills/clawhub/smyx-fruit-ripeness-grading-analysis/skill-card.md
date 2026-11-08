## Description:

Grades tomato and strawberry ripeness from images or videos and returns fruit-level maturity classifications with harvest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers, greenhouse operators, and fruit cooperatives can submit tomato or strawberry images or videos to assess maturity and inform harvest timing. They can also request a Markdown list of prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images and videos are sent to an external service, and its retention practices are unverified.

Mitigation: Avoid uploading sensitive media and review the service's data handling terms before use.

Risk: The documented export-only option still permits uploads.

Mitigation: Do not rely on this option for offline or upload-free use until the behavior is fixed.

Risk: Automatic account setup retains reusable credentials without clear user control.

Mitigation: Seek fixes for account-registration disclosure and protected token storage before installing; restrict credentials to intended destinations.

Risk: The documented --api-url option does not redirect processing to a service selected by the user.

Mitigation: Verify the configured service destination and restrict outbound access; do not assume --api-url changes where data is sent.

## Reference(s):

- [Analysis API response and error codes](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured ripeness analysis; JSON by default and Markdown for report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fruit-level maturity grades, visual observations, harvest guidance, and report links]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
