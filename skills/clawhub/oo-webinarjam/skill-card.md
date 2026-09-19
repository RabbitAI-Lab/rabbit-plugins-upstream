## Description:

Provides agent guidance for using the OOMOL oo CLI to read WebinarJam data and register WebinarJam users through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill when a user asks to list WebinarJam webinars, inspect webinar details or registrants, or register a user after confirmation. It is intended for users operating a connected WebinarJam account through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Review the installer before execution and prefer a pinned, verified install method with checksums or signatures.

Risk: The register_user action changes WebinarJam account state by adding a registrant.

Mitigation: Confirm the exact register_user payload and intended webinar with the user before running the write action.

Risk: A connected WebinarJam account may expose webinar and registrant data to the skill's connector actions.

Mitigation: Connect only the WebinarJam account intended for this workflow and re-check authorization if scopes or credentials change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webinarjam)
- [WebinarJam homepage](https://webinarjam.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
