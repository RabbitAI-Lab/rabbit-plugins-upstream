## Description:

Vincario (vincario.com). Use this skill for ANY Vincario request - searching and reading data. Whenever a task involves Vincario, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Vincario through an OOMOL-connected account for VIN decoding, stolen-vehicle checks, market value estimates, decode-field discovery, and service credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include running a remote oo CLI installer script directly in a shell.

Mitigation: Review and verify the oo CLI installation path before installation, and prefer official package-manager or manually verified installation instructions where available.

Risk: Vincario connector use may depend on OOMOL connection permissions and may consume service credits.

Mitigation: Connect the Vincario account and run actions only after understanding connector permissions and possible credit charges; treat HTTP 402 or insufficient-credit errors as billing stops.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vincario)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vincario homepage](https://vincario.com/)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect Vincario action schemas and run connector actions with JSON payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
