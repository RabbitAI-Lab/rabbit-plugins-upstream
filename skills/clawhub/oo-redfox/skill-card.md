## Description:

RedFoxHub helps agents search and read public user, work, article, comment, and account data from supported social platforms through the OOMOL oo CLI and redfox connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve and search RedFoxHub data from supported social platforms while inspecting live connector schemas before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include online installer commands without built-in integrity checks.

Mitigation: Install the oo CLI only from trusted OOMOL documentation and prefer manual installation with version and integrity checks where available.

Risk: Connector actions can run with user account access and JSON payloads supplied by the agent.

Mitigation: Inspect the live action schema and review the action name and payload before execution, especially for any write or destructive action tags.

## Reference(s):

- [RedFoxHub homepage](https://redfox.hk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub RedFoxHub skill page](https://clawhub.ai/oomol/skills/oo-redfox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector schema checks, connector run commands, JSON payloads, and summarized RedFoxHub results.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
