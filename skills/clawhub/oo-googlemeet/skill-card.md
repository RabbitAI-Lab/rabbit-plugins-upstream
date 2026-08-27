## Description:

Google Meet (workspace.google.com) connector skill for reading, creating, and updating Google Meet data through OOMOL instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected Google Meet account use this skill to inspect live action schemas and run Google Meet connector actions for spaces, conference records, participants, recordings, transcripts, and smart notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports that `end_active_conference` is treated as safe to run directly even though it ends an active meeting.

Mitigation: Require explicit user confirmation of the target meeting space and effect before running it, and treat the action as destructive until it is correctly tagged and scoped.

Risk: Write actions can create or update Google Meet state.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged `[write]`.

Risk: First-time setup, connection, and billing recovery steps may require account-level OOMOL actions.

Mitigation: Run setup or billing guidance only after the matching command failure appears, and direct users through the documented OOMOL auth or connection flow.

## Reference(s):

- [ClawHub Google Meet skill page](https://clawhub.ai/oomol/skills/oo-googlemeet)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Meet homepage](https://workspace.google.com/products/meet/)
- [OOMOL Google Meet connection page](https://console.oomol.com/app-connections?provider=googlemeet)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses `oo connector schema` before `oo connector run`; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
