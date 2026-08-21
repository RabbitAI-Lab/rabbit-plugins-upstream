## Description:

TikTok Shop product selection and creator commerce intelligence: sales and GMV data, goods/live/video-ad monetization signals, product details, creator commerce potential.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External teams, developers, and commerce analysts use this skill to evaluate TikTok Shop creator performance, product opportunities, live commerce, and video-ad monetization signals before planning pilots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User queries, TikTok handles, product IDs, query parameters, and a stable install identifier may be sent to a hosted API service.

Mitigation: Review data-sharing expectations before use, avoid sending sensitive identifiers, and use a trusted SCRUMBALL_BASE_URL/API key only when the request destination is understood.

Risk: The skill creates a persistent local install identifier that may remain across skill reinstallations.

Mitigation: Delete ~/.scrumball_install_id to reset the local identifier when needed.

Risk: Commerce signals can be incomplete or unstable when one data dimension is missing or the sample is limited.

Mitigation: Report reduced confidence, continue only with available dimensions, and scope recommendations as pilots with explicit KPI checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chengyu-xixihaha/skills/influencer-commerce-intel)
- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operation Manifest](artifact/references/operations.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown analysis with optional JSON API responses and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns commerce summary, opportunity, risk, and next-step pilot recommendation.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact/config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
