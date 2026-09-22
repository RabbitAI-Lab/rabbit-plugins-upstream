## Description:

Provides the newest-batch Zhejiang technology-based SME roster, city distribution, and lead-screening data for application agencies, finance and tax service teams, and industrial park sourcing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as application agencies, finance and tax service teams, and industrial park sourcing teams use this skill to query collected Zhejiang technology-based SME roster entries, city distribution, and company lead data.

### Deployment Geography for Use:

Global use; data coverage is limited to Zhejiang Province, China.

## Known Risks and Mitigations:

Risk: Lookup queries are sent to the provider service.

Mitigation: Use the skill only when external provider lookup is acceptable for the user's query and avoid sending unnecessary sensitive information.

Risk: The skill stores product credentials, cookies, and an install ID locally under ~/.odf for session and entitlement handling.

Mitigation: Protect the local credential file and rotate or remove stored credentials when access should be revoked.

Risk: Roster results cover only the collected portion of Zhejiang Province technology-based SME data and may not represent the full official roster.

Mitigation: Present coverage notes with results and treat a missed query as not found in the collected dataset rather than proof that an entity is absent from the official roster.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/zj-sme-roster)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text summarizing roster matches, city distribution, coverage notes, and setup or network-status guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Queries are sent to the provider service; product credentials, cookies, and an install ID may be stored locally under ~/.odf for session and entitlement handling.]

## Skill Version(s):

1.0.4 (source: frontmatter, manifest, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
