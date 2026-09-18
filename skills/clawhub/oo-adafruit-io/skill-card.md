## Description:

Adafruit IO (io.adafruit.com) skill for reading account and feed information and creating feed data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Adafruit IO account and feed information, list feed data, and create feed data through the OOMOL Adafruit IO connector. Write actions should be run only after confirming the exact target feed and payload with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Review first-time setup before installing; prefer a verified oo CLI package or release path, or inspect and verify the installer before running it.

Risk: The create_feed_data action can change Adafruit IO feed state.

Mitigation: Confirm the exact feed target and JSON payload with the user before running the write action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-adafruit-io)
- [Adafruit IO Homepage](https://io.adafruit.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
