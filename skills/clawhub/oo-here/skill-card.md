## Description:

HERE (here.com). Use this skill for ANY HERE request - searching and reading data. Whenever a task involves HERE, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search HERE places and addresses, geocode queries, reverse-geocode coordinates, and look up HERE locations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute directly in a shell.

Mitigation: Use an official, versioned installation method with verification before executing installer content.

Risk: HERE requests are routed through OOMOL as an intermediary with credentials managed server-side by OOMOL.

Mitigation: Install only when this credential and request-routing model is acceptable for the intended data and account scopes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-here)
- [HERE homepage](https://www.here.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing HERE connector payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
