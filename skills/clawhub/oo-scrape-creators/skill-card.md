## Description:

Helps agents operate Scrape Creators through an OOMOL-connected account for endpoint discovery, credit checks, and documented API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search and read Scrape Creators data by inspecting connector schemas, building JSON payloads, and running documented connector actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts in a shell.

Mitigation: Prefer official versioned, signed, or checksum-verified installation steps and review installer contents before execution.

Risk: The skill can invoke documented Scrape Creators GET and POST endpoints through an authenticated OOMOL-connected account.

Mitigation: Inspect the live connector schema before building payloads, confirm the exact payload and effect before any write or destructive action, and avoid exposing raw credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrape-creators)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Scrape Creators homepage](https://scrapecreators.com/)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector JSON responses returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
