## Description:

Bloomerang helps agents search and read Bloomerang constituent and household data through an OOMOL-connected Bloomerang account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and search Bloomerang constituent or household records from a connected Bloomerang account without handling raw API credentials. It supports read-only get, list, and search workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that would execute code locally.

Mitigation: Install the oo CLI through a pinned, verifiable release or trusted package manager, and run remote installer scripts only after independently trusting the source and expected local changes.

Risk: Connector payloads can become inaccurate if the live Bloomerang action schema changes.

Mitigation: Inspect the live connector schema before building each payload, as the artifact instructs.

Risk: Future connector actions tagged write or destructive could modify or remove Bloomerang data.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Bloomerang homepage](https://bloomerang.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bloomerang)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before constructing payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
