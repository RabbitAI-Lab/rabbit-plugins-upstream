## Description:

BambooHR helps agents search and read BambooHR company and employee data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business operators use this skill to retrieve BambooHR company information, employee records, employee lists, and available employee fields through a connected BambooHR account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes that setup instructions can execute unverified remote installer scripts.

Mitigation: Prefer installing the oo CLI from a signed, versioned, or package-managed source before using this skill.

Risk: The security review notes that the invocation scope is broad for sensitive HR data.

Mitigation: Use this skill only for explicit BambooHR data requests and review requested fields before retrieving employee information.

## Reference(s):

- [BambooHR homepage](https://www.bamboohr.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live BambooHR connector schemas before executing read actions.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
