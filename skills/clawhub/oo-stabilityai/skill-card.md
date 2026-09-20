## Description:

Stability AI (stability.ai). Use this skill for ANY Stability AI request -- reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Stability AI through an OOMOL-connected account, including generating audio from a text prompt after inspecting the live action schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Stability AI actions through OOMOL as an intermediary.

Mitigation: Install only when the user is comfortable using OOMOL for Stability AI actions and understands that credentials are injected through the connector.

Risk: The listed action can create generated audio and upload it to connector transit storage.

Mitigation: Confirm the exact prompt, action payload, and intended effect with the user before running write actions.

Risk: First-time setup may involve running an installer script.

Mitigation: Review OOMOL's install instructions or verify the installer source before running the installer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-stabilityai)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Stability AI Homepage](https://stability.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces oo CLI commands that inspect connector schemas and run Stability AI actions; generated audio is uploaded to connector transit storage.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
