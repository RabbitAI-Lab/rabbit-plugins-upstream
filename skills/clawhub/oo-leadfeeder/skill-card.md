## Description:

Leadfeeder (leadfeeder.com). Use this skill for ANY Leadfeeder request — searching and reading data. Whenever a task involves Leadfeeder, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Leadfeeder through an OOMOL-connected account for company enrichment, account lookup, company matching, and firmographic search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes one-line remote installer commands that can execute changing code on a user's machine.

Mitigation: Prefer official, versioned installation instructions with a signed package or checksum verification before installing the oo CLI.

Risk: Leadfeeder data flows through the OOMOL connector using server-side credentials.

Mitigation: Install only if you trust OOMOL, and connect only the Leadfeeder account and scopes needed for the intended task.

## Reference(s):

- [Leadfeeder homepage](https://www.leadfeeder.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-leadfeeder)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the oo CLI and may return Leadfeeder JSON data.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
