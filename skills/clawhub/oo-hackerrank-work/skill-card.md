## Description:

Use this skill for HackerRank Work searching and reading tasks through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and recruiting operations users use this skill to search and retrieve HackerRank Work tests and test candidates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review first-time setup before installation, prefer a verified and version-pinned oo CLI installer from the vendor, and avoid running remote installer commands from an elevated shell.

Risk: Future connector actions could change HackerRank Work state if they are introduced and tagged as write or destructive.

Mitigation: Keep routine use limited to the currently documented read actions unless a future version clearly documents state-changing actions and the user confirms the exact payload and effect.

## Reference(s):

- [HackerRank Work homepage](https://www.hackerrank.com/work)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [HackerRank Work ClawHub listing](https://clawhub.ai/oomol/skills/oo-hackerrank-work)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads; read actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
