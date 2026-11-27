## Description:

Automates B2B account discovery and personalized email generation using the Alpha Ceema database via direct API access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alphaceema](https://clawhub.ai/user/alphaceema)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business development users use this skill to discover target companies, enrich account details, and draft personalized B2B outreach emails from Alpha Ceema company data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may make outbound requests to the Alpha Ceema API and use returned company data in generated sales outreach.

Mitigation: Install only if this network access is acceptable, and review generated outreach for compliance and accuracy before use.

Risk: Generated outreach may be inaccurate, overly generic, or unsuitable for the recipient context.

Mitigation: Human reviewers should verify company details and adjust messaging before sending.

## Reference(s):

- [Alpha Ceema B2B Outreach API base URL](https://us-central1-openclaw-b2b-outreach.cloudfunctions.net/api/api/v1)
- [ClawHub skill page](https://clawhub.ai/alphaceema/skills/skill)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text with outbound GET requests to the Alpha Ceema API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use public company data returned by the API to draft outreach; generated emails should be reviewed for compliance and accuracy.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
