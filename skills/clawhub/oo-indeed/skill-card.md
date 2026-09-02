## Description:

Enables an agent to operate Indeed employer accounts through OOMOL, including reading user, employer, and job data and performing approved job posting updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to inspect Indeed employer account data, list or retrieve jobs, or carry out user-approved updates to sourced job postings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can update or clear Indeed job posting data.

Mitigation: Review the exact action payload and get explicit user approval before running write or destructive actions.

Risk: The skill depends on an OOMOL-connected Indeed employer account.

Mitigation: Install it only for workflows that intentionally use OOMOL to access Indeed, and resolve authentication or connection errors through the documented setup path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-indeed)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Indeed homepage](https://www.indeed.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
