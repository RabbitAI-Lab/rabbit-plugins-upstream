## Description:

WaiverForever (waiverforever.com). Use this skill for ANY WaiverForever request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate WaiverForever through an OOMOL-connected account, including reading account data, templates, waiver requests, and signed waivers, and creating template signing links or waiver request groups after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run unverified remote installer scripts.

Mitigation: Review the installer path first and prefer a verified package, pinned release, checksum, or signature-backed installation method for the oo CLI.

Risk: WaiverForever write actions can create signing links or waiver request groups.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [WaiverForever homepage](https://www.waiverforever.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [WaiverForever skill on ClawHub](https://clawhub.ai/oomol/skills/oo-waiverforever)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts the agent to inspect live connector schemas before building payloads and to confirm WaiverForever write actions before execution.]

## Skill Version(s):

1.0.2 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
