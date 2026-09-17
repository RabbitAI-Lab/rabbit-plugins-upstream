## Description:

BambooHR helps agents search and read company and employee data from a connected BambooHR account through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business operators use this skill to retrieve BambooHR company profile details, employee records, employee lists, and available employee fields from an already connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts that can be piped directly into a shell.

Mitigation: Prefer a pinned, signed, or checksum-verified oo CLI installation path before using the skill.

Risk: BambooHR reads are mediated through OOMOL as the connected account provider.

Mitigation: Use the skill only where OOMOL is approved as an intermediary for BambooHR data access and limit use to BambooHR account data tasks.

## Reference(s):

- [ClawHub BambooHR skill](https://clawhub.ai/oomol/skills/oo-bamboohr)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [BambooHR homepage](https://www.bamboohr.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; responses may include BambooHR account data returned as JSON.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
