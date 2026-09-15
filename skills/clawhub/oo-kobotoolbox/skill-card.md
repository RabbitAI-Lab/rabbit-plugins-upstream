## Description:

KoboToolbox lets an agent read, create, update, deploy, export, validate, and delete KoboToolbox projects and submissions through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage KoboToolbox survey projects and submissions from an OOMOL-connected account while inspecting live action schemas before write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute code on the user's machine.

Mitigation: Review setup instructions before installing and prefer a verified or package-manager installation path where available.

Risk: Write and destructive KoboToolbox actions can change, overwrite, or permanently delete project and submission data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [KoboToolbox homepage](https://www.kobotoolbox.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kobotoolbox)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.3 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
