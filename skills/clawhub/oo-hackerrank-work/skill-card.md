## Description:

HackerRank Work helps agents search and read HackerRank Work tests and candidate data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, hiring operations staff, and recruiting teams use this skill to retrieve HackerRank Work tests, list or search test candidates, and inspect candidate records from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include installing the oo CLI through a remote shell script, which could expose users to unverified installer behavior.

Mitigation: Install only from a trusted OOMOL distribution path and prefer a verified package or release process instead of piping a downloaded script directly into a shell.

Risk: The connector processes HackerRank Work data through an OOMOL-connected account.

Mitigation: Use the skill only with trusted OOMOL account connections and review organization data-handling expectations before running connector actions.

## Reference(s):

- [HackerRank Work homepage](https://www.hackerrank.com/work)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hackerrank-work)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
