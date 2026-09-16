## Description:

Gender-API.com helps an agent query Gender-API.com through an OOMOL-connected account for gender, country-of-origin, ethnicity, and account-usage lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Gender-API.com lookups for names or email addresses, retrieve country-of-origin and ethnicity metadata, and check connected-account usage statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can execute unverified remote installer scripts.

Mitigation: Review the oo CLI installation method before use and prefer a signed, checksummed, or package-managed installer.

Risk: Gender, country-of-origin, ethnicity, and account lookups may transfer personal data such as names, email addresses, IP addresses, locale hints, and caller IDs.

Mitigation: Confirm the user intends this processing before running queries and send only the fields needed for the requested lookup.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gender-api)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Gender-API.com Homepage](https://gender-api.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include Gender-API.com result data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
