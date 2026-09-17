## Description:

Helps agents search and read Humaans people data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operations teams, and developers use this skill to retrieve Humaans profile records, list people with filters, and inspect token scopes from a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive HR data available to the connected Humaans account.

Mitigation: Install only if the publisher is trusted, keep the Humaans connection limited to the least scopes needed, and review retrieved data handling before use.

Risk: The first-time setup section documents remote installer commands for the oo CLI.

Mitigation: Prefer a verified or package-manager installation path for the oo CLI before relying on remote installation scripts.

Risk: Future write or destructive Humaans actions could change account data.

Mitigation: Require explicit user confirmation of the exact payload and effect before running any write or destructive action.

## Reference(s):

- [Humaans homepage](https://humaans.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-humaans)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for invoking live Humaans connector actions; connector responses are JSON.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
