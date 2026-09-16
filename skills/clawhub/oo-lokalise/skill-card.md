## Description:

Lokalise (lokalise.com). Use this skill for Lokalise requests, including reading, creating, updating, and deleting data through OOMOL-connected actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and localization teams use this skill to manage Lokalise projects, keys, languages, and translations through an OOMOL-connected oo CLI session while avoiding direct handling of raw Lokalise API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute mutable remote installer scripts locally.

Mitigation: Review the installer path before installing, prefer a verified package or signed release, and only run the shell or PowerShell installer if the OOMOL distribution endpoint is trusted.

Risk: Write actions can change Lokalise project data.

Mitigation: Confirm the exact project, key, translation, and payload before running create or update actions.

Risk: The destructive delete_key action removes a Lokalise key.

Mitigation: Require explicit approval for the target project and key ID before running delete_key.

Risk: Action payloads may be invalid if the agent assumes a stale schema.

Mitigation: Inspect the live action schema with oo connector schema before constructing each payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lokalise)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Lokalise](https://lokalise.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON action payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use oo connector schema and oo connector run; write and destructive actions require confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release evidence, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
