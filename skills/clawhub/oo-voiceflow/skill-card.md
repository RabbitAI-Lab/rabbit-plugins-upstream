## Description:

Voiceflow (voiceflow.com). Use this skill for ANY Voiceflow request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Voiceflow connector schemas, run JSON-based Voiceflow actions, manage conversation sessions, list environments, and query knowledge bases through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to execute an internet-downloaded installer for the oo CLI.

Mitigation: Use official, versioned, and verified OOMOL installation instructions where available; avoid elevated shells during installation.

Risk: Voiceflow actions tagged as write can change connected Voiceflow state.

Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Voiceflow skill page](https://clawhub.ai/oomol/skills/oo-voiceflow)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Voiceflow homepage](https://www.voiceflow.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL oo CLI connector schemas before constructing action payloads; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.2 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
