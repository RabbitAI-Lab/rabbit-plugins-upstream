## Description:

Needle helps an agent operate Needle through the OOMOL-connected oo CLI for listing collections, retrieving details and stats, managing URL-backed files, creating collections, and searching indexed content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with Needle collections through an authenticated OOMOL connector, including read workflows for collection inspection and search plus confirmed write workflows for collection creation and file import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes one-line remote installer commands that execute downloaded scripts.

Mitigation: Review the installer source before use and prefer a signed, pinned, or manually verified oo CLI installation path when available.

Risk: Write actions can create collections or import URL-backed files into Needle.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Needle homepage](https://needle.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-needle)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payloads; read actions can run directly, while write actions require confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
