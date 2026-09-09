## Description:

Automates B2B account discovery and personalized email generation using the Alpha Ceema database via direct API access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alphaceema](https://clawhub.ai/user/alphaceema)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and go-to-market agents use this skill to discover target companies, enrich account context, and draft personalized B2B outreach emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may use company data returned by Alpha Ceema in bulk sales workflows that are subject to privacy, data-licensing, or anti-spam obligations.

Mitigation: Review the intended audience, data use, and sending process for compliance with applicable privacy, licensing, and anti-spam rules before using the skill at scale.

Risk: Generated outreach emails may contain inaccurate, outdated, or unsuitable personalization.

Mitigation: Review and edit generated emails before sending them to prospects.

## Reference(s):

- [Alpha Ceema B2B Outreach API](https://us-central1-openclaw-b2b-outreach.cloudfunctions.net/api/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text account lists and outreach drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API query parameters and pagination cursors when needed.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
