## Description:

Axiom helps an agent inspect live connector schemas and operate Axiom datasets and APL queries through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, create, retrieve, and delete Axiom datasets, and to run Axiom Processing Language queries from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer one-liners for the oo CLI.

Mitigation: Review the installer path before use and prefer a verified, versioned, or signed release where available.

Risk: The skill can create or delete Axiom datasets.

Mitigation: Confirm the exact payload and target before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [Axiom homepage](https://axiom.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Axiom skill on ClawHub](https://clawhub.ai/oomol/skills/oo-axiom)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
