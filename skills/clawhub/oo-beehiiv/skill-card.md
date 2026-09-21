## Description:

Beehiiv (beehiiv.com). Use this skill for ANY Beehiiv request - searching and reading data. Whenever a task involves Beehiiv, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search and read Beehiiv publications, posts, and subscriptions through an OOMOL-connected Beehiiv account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Beehiiv account data through an OOMOL-connected account.

Mitigation: Install and use it only when OOMOL and the connected Beehiiv account are trusted for the intended read-only queries.

Risk: The first-time setup path includes shell-piped installer commands for the oo CLI.

Mitigation: Review the oo CLI installation source or use the documented install guide before running installer commands.

Risk: Future Beehiiv connector actions could change or remove account data if tagged as write or destructive.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Beehiiv Skill](https://clawhub.ai/oomol/skills/oo-beehiiv)
- [Beehiiv Homepage](https://www.beehiiv.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Beehiiv connector schemas before building action payloads; current documented actions are read-oriented get and list operations.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
