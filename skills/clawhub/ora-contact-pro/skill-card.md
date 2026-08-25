## Description:

Helps users perform authorized, compliant foreign-trade prospecting and decision-maker lookup by company name, company domain, or LinkedIn company identifier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oraagent](https://clawhub.ai/user/oraagent)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and company-research users use this skill to retrieve company profiles, contact channels, social links, and limited employee or decision-maker leads when they have authorization and a compliant outreach purpose.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends company, domain, or LinkedIn-company queries to Topeasy's external API using a local OraAgent.key.

Mitigation: Use the skill only when the user accepts that external data processing and has authorization for the lookup.

Risk: Saved JSON result files may contain business contact data or sensitive outreach-relevant details.

Mitigation: Limit display to necessary fields and remove temporary result files when they are no longer needed.

Risk: Returned contact information could be misused for unauthorized collection, spam, harassment, or privacy-invasive outreach.

Mitigation: Use only for compliant company research and stop when authorization or legal basis is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oraagent/skills/ora-contact-pro)
- [OraAgent publisher profile](https://clawhub.ai/user/oraagent)
- [Topeasy platform](https://www.oraskl.com/platform)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown summary with references to saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include company details, contact channels, social links, employee/contact summaries, empty-result notices, and API status errors.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
