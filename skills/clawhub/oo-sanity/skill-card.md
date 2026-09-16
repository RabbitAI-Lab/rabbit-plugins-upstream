## Description:

Enables agents to query Sanity documents and run approved Sanity document mutations through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to retrieve Sanity documents, run GROQ queries, and perform explicitly approved document mutations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform Sanity mutations even though normal use may look read-oriented.

Mitigation: Require the user to request the mutation, review the exact payload and effect, and approve it before execution.

Risk: Installer examples include remote pipe-to-shell commands.

Mitigation: Prefer a verified oo CLI release or package-manager installation path before using the skill.

Risk: An agent using the skill can act through the connected OOMOL Sanity account.

Mitigation: Install and use the skill only where that account access is intended, and keep mutation use narrowly scoped to explicit requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sanity)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sanity homepage](https://www.sanity.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands depend on live oo connector schemas and the connected OOMOL Sanity account state.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
