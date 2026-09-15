## Description:

Apiframe lets an agent operate Apiframe through the OOMOL oo CLI connector to submit generation jobs and inspect models or job status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Apiframe from an OOMOL-connected account, including listing models, submitting image, music, or video generation jobs, and tracking job results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation actions can submit remote Apiframe jobs and may consume account credits.

Mitigation: Treat generate_image, generate_music, and generate_video as write operations and confirm the payload and intended effect with the user before execution.

Risk: First-time setup examples pipe remote installer scripts directly into shells.

Mitigation: Do not run curl|bash or irm|iex installer commands unless the installer is independently trusted and verified; prefer a safer manual or package-manager installation path.

Risk: Incorrect payloads can be sent if an agent assumes an action schema.

Mitigation: Fetch the live connector schema for the selected action before constructing or running a payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-apiframe)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Apiframe Homepage](https://apiframe.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires inspecting the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
