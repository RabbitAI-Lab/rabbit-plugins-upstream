## Description:

Find and verify work emails from a name and company — waterfall lookup across providers, one call for agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find a person's professional email, verify deliverability before outreach, or list known addresses for a company domain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Superagnt API key and sends contact lookup or verification data to Superagnt.

Mitigation: Install only when that data sharing is acceptable, keep SUPERAGNT_API_KEY scoped and protected, and avoid submitting sensitive contact data unless permitted.

Risk: The security review notes that the skill encourages enabling broader Superagnt platform tools beyond email lookup.

Mitigation: Keep enabled MCP tools limited to email finding, verification, and domain email listing unless broader platform access is intentionally approved.

## Reference(s):

- [Email Finder documentation](https://superagnt.com/r/ch-email-finder-docs)
- [Email Finder ClawHub listing](https://clawhub.ai/jaencarrodine/skills/email-finder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API calls.]

## Skill Version(s):

2.0.5 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
