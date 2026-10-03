## Description:

TypeSafe AI (typesafe.ai). Use this skill for TypeSafe AI requests by inspecting live connector schemas and running TypeSafe AI actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to evaluate text or structured JSON with TypeSafe AI and list available TypeSafe models through the connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text or structured JSON supplied by the user may be sent to the external TypeSafe AI connector through the connected OOMOL account.

Mitigation: Only submit data intended for TypeSafe AI evaluation and avoid secrets or sensitive documents unless that sharing is approved.

Risk: The first-time setup guidance includes pipe-to-shell CLI installation commands.

Mitigation: Install the oo CLI through a verified method and inspect or validate the installer before running it.

Risk: The skill can act through the user's OOMOL-connected TypeSafe AI account.

Mitigation: Use the live action schema, confirm any state-changing action payload before execution, and keep account access scoped to the intended TypeSafe AI use.

## Reference(s):

- [TypeSafe AI homepage](https://typesafe.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-typesafe-ai)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
