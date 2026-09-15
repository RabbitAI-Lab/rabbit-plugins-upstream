## Description:

Merriam-Webster Collegiate (merriam-webster.com). Use this skill for ANY Merriam-Webster Collegiate request -- searching and reading data. Whenever a task involves Merriam-Webster Collegiate, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up words in the Merriam-Webster Collegiate Dictionary through an OOMOL-connected account. It supports dictionary entry retrieval and spelling suggestions through the collegiate connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer setup commands can execute high-impact local code.

Mitigation: Install the oo CLI only from verified official releases or trusted package-manager instructions, and do not allow an agent to run remote installer commands automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-collegiate)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Merriam-Webster Collegiate homepage](https://www.merriam-webster.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include dictionary entries, spelling suggestions, connector execution metadata, and setup guidance for authentication, connection, or billing failures.]

## Skill Version(s):

1.0.4 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
