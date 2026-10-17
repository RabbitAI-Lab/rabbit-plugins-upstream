## Description:

Assesses post-grooming pet images or videos for mats, dandruff, and coat smoothness, then provides a grooming score and follow-up suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and grooming professionals use this skill to review post-grooming photos or videos, check for remaining mats and dandruff, and decide whether additional grooming is needed. It can also retrieve prior assessment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or media URLs are sent to a cloud service for analysis, and historical reports are queried remotely.

Mitigation: Obtain user consent for remote processing and avoid submitting sensitive media or URLs unless that transfer is acceptable.

Risk: The skill can silently create or reuse an account identity and cache returned tokens in a local workspace database.

Mitigation: Disclose account-linking and local token storage before use; restrict access to the workspace and use the skill only if those behaviors are acceptable.

## Reference(s):

- [Grooming assessment API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured assessment results in JSON or readable text; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a grooming score, observations, care suggestions, and report links when available; results are not a medical diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
