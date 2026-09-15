## Description:

Wufoo (wufoo.com). Use this skill for ANY Wufoo request: reading, creating, and updating data through the OOMOL-connected Wufoo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Wufoo action schemas, list forms and entries, retrieve form fields, count entries, and submit new form entries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts directly in a shell.

Mitigation: Install the oo CLI only from a trusted source and prefer downloading and verifying the installer before execution.

Risk: The submit_entry action creates new Wufoo entries and can change production form data.

Mitigation: Review the exact payload and intended effect with the user before approving submit_entry.

## Reference(s):

- [Wufoo homepage](https://www.wufoo.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Wufoo skill page](https://clawhub.ai/oomol/skills/oo-wufoo)
- [Wufoo icon](https://static.oomol.com/logo/third-party/wufoo.svg)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI schema commands, connector run commands, JSON request payloads, and guidance for reviewing write actions before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
