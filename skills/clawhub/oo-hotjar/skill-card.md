## Description:

This skill lets agents read Hotjar survey data and submit user lookup requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to inspect Hotjar action schemas, retrieve surveys and survey responses, and run approved user lookup requests from a connected Hotjar account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution channel, preferably with a verified and version-pinned method.

Risk: The user lookup action can change Hotjar state and may delete matching data when deletion is requested.

Mitigation: Confirm the exact payload and effect with the user before running write actions, and require explicit approval before any deletion.

## Reference(s):

- [ClawHub Hotjar skill page](https://clawhub.ai/oomol/skills/oo-hotjar)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Hotjar homepage](https://www.hotjar.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON data and execution metadata when commands are run.]

## Skill Version(s):

1.0.2 (source: evidence.json release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
