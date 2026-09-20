## Description:

Hex lets agents inspect Hex projects and API-triggered runs, trigger published project runs, and cancel in-progress runs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to manage Hex project metadata and API-triggered project runs from an agent workflow, including listing projects, checking run status, starting runs, and canceling in-progress runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the OOMOL CLI.

Mitigation: Do not let an agent run the installer automatically; review official install instructions, use a pinned release when possible, and verify integrity before installation.

Risk: The skill can trigger Hex project runs and cancel in-progress runs.

Mitigation: Confirm every run_project or cancel_run action, including the target project or run and the expected effect, before execution.

## Reference(s):

- [ClawHub Hex skill page](https://clawhub.ai/oomol/skills/oo-hex)
- [Hex homepage](https://hex.tech)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses that include action data and an execution identifier.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
