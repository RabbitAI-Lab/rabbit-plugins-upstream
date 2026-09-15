## Description:

Adafruit IO helps agents read, create, and update Adafruit IO data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read Adafruit IO account and feed data, list feed data, and create feed data through schema-checked oo CLI calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts that may be run directly in a shell.

Mitigation: Review the installer path before use and prefer a verified, pinned, or signed oo CLI release.

Risk: The skill can create Adafruit IO feed data.

Mitigation: Confirm the exact feed, payload, and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-adafruit-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Adafruit IO](https://io.adafruit.com/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running Adafruit IO connector actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
