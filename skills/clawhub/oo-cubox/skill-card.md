## Description:

Cubox (cubox.pro). Use this skill for ANY Cubox request: reading, creating, and updating data through an OOMOL-connected Cubox account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cubox from an agent workflow, including saving web pages for queued parsing and snapshot processing through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask the agent to execute a remote installer for the OOMOL oo CLI.

Mitigation: Install only after independently trusting OOMOL's oo CLI installer; prefer reviewing the installer or using an official package or pinned release.

Risk: The save_url action changes Cubox state by saving content.

Mitigation: Confirm the exact URL payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Cubox Skill](https://clawhub.ai/oomol/skills/oo-cubox)
- [Cubox Homepage](https://cubox.pro)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
