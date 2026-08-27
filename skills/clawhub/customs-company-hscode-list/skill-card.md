## Description:

Queries UpKuaJing customs data for a company's paginated HS-code trade breakdown, including trade counts, amounts, quantities, weights, and percentage share by HS code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External trade analysts, sourcing teams, and agent users use this skill to inspect a supplier or buyer's product mix by company ID, page through HS-code rows, and filter by dates, products, HS codes, or countries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an UpKuaJing API key in a plaintext home-directory .env file.

Mitigation: Use a dedicated API key where possible, restrict access to the local account, and rotate the key if the machine or workspace is shared.

Risk: The skill can make paid UpKuaJing API calls after confirmation and can create top-up payment URLs on request.

Mitigation: Require explicit user confirmation before paid queries or top-up flows, and check current pricing before use.

Risk: The skill can send optional error reports to UpKuaJing and performs an automatic version check during API use.

Mitigation: Confirm before reporting errors and disclose that API script runs may contact UpKuaJing for version checks.

## Reference(s):

- [Company HS Code List API](references/customs-company-hscode-list-api.md)
- [Skill Error Report API](references/skill-error-report-api.md)
- [UpKuaJing Homepage](https://www.upkuajing.com)
- [UpKuaJing Open Platform](https://developer.upkuajing.com/)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/customs-company-hscode-list)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; query calls may incur fees and return paginated results with cursor-based continuation.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
