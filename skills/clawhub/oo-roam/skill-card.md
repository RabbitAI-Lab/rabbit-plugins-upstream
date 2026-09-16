## Description:

Roam HQ (ro.am). Use this skill for Roam HQ requests involving reading, creating, and updating data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate Roam HQ through an OOMOL-connected account, including listing groups, magicasts, and recordings, retrieving magicasts, and sending group messages after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions execute remote installer scripts directly, which can expose users to unverified code execution.

Mitigation: Install the oo CLI from a verified release, signed package, or separately downloaded installer that can be inspected, and avoid running setup commands from an elevated shell.

Risk: The send_message action changes Roam HQ state by posting to a group as a bot.

Mitigation: Confirm the exact target group, payload, and expected effect with the user before running write actions.

## Reference(s):

- [Roam HQ homepage](https://ro.am)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Roam HQ skill page](https://clawhub.ai/oomol/skills/oo-roam)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses from Roam HQ connector actions.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
