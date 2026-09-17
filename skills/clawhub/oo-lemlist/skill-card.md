## Description:

lemlist (lemlist.com). Use this skill for ANY lemlist request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect lemlist campaigns, campaign leads, and team information through an OOMOL-connected account using the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can lead an agent to run remote installer scripts for the oo CLI.

Mitigation: Do not allow automatic execution of installer commands; verify the source, prefer a pinned release or package manager, and approve installation manually.

Risk: Authentication and connection setup may open account or credential flows.

Mitigation: Run login and lemlist connection steps only after a command fails for that reason, and have the user confirm the account and connection state directly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lemlist)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [lemlist homepage](https://www.lemlist.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [lemlist icon](https://static.oomol.com/logo/third-party/lemlist.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides schema inspection and read-only connector runs that return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
