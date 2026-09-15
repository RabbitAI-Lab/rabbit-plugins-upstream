## Description:

Use HR Partner through OOMOL to search and read employee, recruiting, company, and lookup data via the hr_partner connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents supporting HR workflows use this skill to retrieve HR Partner employee records, applicant and application details, job listings, company metadata, and lookup values through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive HR employee and recruiting data through the HR Partner connector.

Mitigation: Use an HR Partner account with permissions limited to the employee and applicant data the agent is intended to read.

Risk: The first-time setup instructions include pipe-to-shell CLI installation commands.

Mitigation: Prefer a verified, pinned, or package-manager installation of the oo CLI instead of running remote installer scripts directly.

Risk: The connector depends on OOMOL-managed credentials and account connection state.

Mitigation: Only install and use the skill if OOMOL is trusted for this workflow, and resolve authentication or connection failures through the documented account flow.

## Reference(s):

- [ClawHub HR Partner Skill Page](https://clawhub.ai/oomol/skills/oo-hr-partner)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [HR Partner Homepage](https://www.hrpartner.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payload instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing JSON payloads and returns HR Partner connector responses as JSON.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
