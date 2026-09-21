## Description:

This skill lets agents search and read SportsDataIO data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query SportsDataIO through an OOMOL-connected account for sports, competitions, seasons, teams, athletes, venues, schedules, and event results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path asks the agent to install a remote CLI script into the user's environment.

Mitigation: Review the oo CLI installation path first, prefer official verifiable install instructions, and confirm setup steps before allowing installation commands.

Risk: SportsDataIO access depends on an authenticated OOMOL account and connected SportsDataIO credentials.

Mitigation: Run read actions only after the user has installed and signed in to the oo CLI, and use setup or connection steps only when a command fails with an authentication or connection error.

## Reference(s):

- [SportsDataIO homepage](https://sportsdata.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sportsdata)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas and run SportsDataIO connector actions; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
