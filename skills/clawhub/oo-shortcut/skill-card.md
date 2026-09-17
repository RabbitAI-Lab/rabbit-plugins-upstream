## Description:

Shortcut helps agents read, create, and update Shortcut workspace data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Shortcut workspaces through approved connector actions for stories, epics, projects, members, and workflows. It supports read operations directly and requires confirmation before create or update actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup path includes unverified remote installer commands for the oo CLI when the CLI is missing.

Mitigation: Install the oo CLI only through a trusted, verified method and avoid letting an agent run installer commands automatically.

Risk: Shortcut create and update actions can change workspace state.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [Shortcut skill page](https://clawhub.ai/oomol/skills/oo-shortcut)
- [Shortcut homepage](https://www.shortcut.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Shortcut connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
