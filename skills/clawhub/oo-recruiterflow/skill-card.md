## Description:

Recruiterflow (recruiterflow.com). Use this skill for ANY Recruiterflow request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams and agents use this skill to search and read Recruiterflow candidates, jobs, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to run an unverified remote installer for the oo CLI.

Mitigation: Use a verified installation method for the oo CLI when available and avoid running installer commands from an elevated shell.

Risk: Recruiterflow data is accessed through OOMOL's connector using the user's connected account.

Mitigation: Connect only the intended Recruiterflow account and confirm account scope before retrieving candidate, job, or user data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-recruiterflow)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Recruiterflow Homepage](https://recruiterflow.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Recruiterflow Connection](https://console.oomol.com/app-connections?provider=recruiterflow)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads Recruiterflow data through the oo CLI using schemas fetched before action execution.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
