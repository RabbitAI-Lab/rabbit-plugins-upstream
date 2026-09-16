## Description:

Indeed (indeed.com). Use this skill for ANY Indeed request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an OOMOL-connected Indeed account from an agent, including reading account, employer, and job data and updating sourced job postings after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read employer and job data from the connected Indeed account.

Mitigation: Install and use it only with an OOMOL account and Indeed connection trusted for that data access.

Risk: Write and destructive actions can change or clear sourced job posting updates.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running tagged write or destructive actions.

Risk: The setup guidance includes remote installer commands.

Mitigation: Avoid pipe-to-shell installation unless the installer source and contents have been independently verified.

## Reference(s):

- [Indeed homepage](https://www.indeed.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-indeed)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
