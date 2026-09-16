## Description:

Persona helps agents read, create, list, and update Persona inquiries through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Persona inquiries from an agent, including retrieval, listing, creation, and updates through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance may lead users to run an unverified internet installer directly in a shell.

Mitigation: Prefer a verified oo CLI install path with checksums or signed packages before installation.

Risk: Create and update actions can change Persona inquiry state.

Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect before executing write actions.

## Reference(s):

- [Persona homepage](https://withpersona.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
