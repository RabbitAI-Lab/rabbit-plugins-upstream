## Description:

Leexi enables agents to search and read Leexi calls, meetings, call notes, teams, and users through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve Leexi call and meeting records, call notes, teams, and users after the user has connected Leexi through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Do not run those installer commands blindly; install the oo CLI only from a trusted, verified source or package-manager path.

Risk: The skill can read Leexi workspace call, meeting, call-note, team, and user data through the connected account.

Mitigation: Keep account authentication and Leexi connection steps under explicit user control, and run only the read action needed for the user's request.

## Reference(s):

- [ClawHub Leexi Skill Page](https://clawhub.ai/oomol/skills/oo-leexi)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Leexi Homepage](https://www.leexi.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action execution; command responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
