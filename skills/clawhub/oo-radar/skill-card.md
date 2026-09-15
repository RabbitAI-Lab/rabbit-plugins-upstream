## Description:

Radar supports address, place, and geocoding workflows through an OOMOL-connected Radar account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Radar connector schemas, build matching JSON payloads, and run Radar actions such as autocomplete, forward geocoding, reverse geocoding, IP geocoding, and place search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands that could run arbitrary code if the installer delivery path is compromised.

Mitigation: Prefer a package manager, pinned release, checksum or signature verification, and review of the installer before execution.

Risk: Some Radar connector actions can change state.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions, and require explicit approval for destructive actions.

## Reference(s):

- [Radar homepage](https://radar.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Radar ClawHub release](https://clawhub.ai/oomol/skills/oo-radar)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live Radar connector schema inspection before running actions.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
