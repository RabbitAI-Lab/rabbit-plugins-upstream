## Description:

VBOUT (vbout.com). Use this skill for reading, creating, updating, and deleting VBOUT email marketing data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to inspect VBOUT connector schemas and run account, list, and contact actions through an OOMOL-connected VBOUT account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup examples include one-line remote installers, and the authoritative security summary flags local execution risks.

Mitigation: Install only after independently trusting and inspecting the installer; prefer documented installation steps and avoid running remote install commands blindly.

Risk: VBOUT write and destructive actions can create, update, or delete contact records.

Mitigation: Inspect the live action schema, pass JSON via a reviewed file such as --data @payload.json, and require explicit user approval before write or delete actions.

Risk: The skill operates through connected OOMOL and VBOUT accounts.

Mitigation: Install only when account access through OOMOL and VBOUT is acceptable for the deployment context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vbout)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [VBOUT homepage](https://www.vbout.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and artifact frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
