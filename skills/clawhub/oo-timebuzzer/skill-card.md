## Description:

timeBuzzer (timebuzzer.com). Use this skill for ANY timeBuzzer request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage timeBuzzer account data through OOMOL's oo CLI, including reading user details, activities, layers, and tiles, and creating, updating, or deleting activities after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to run remote installer scripts for the OOMOL oo CLI.

Mitigation: Review OOMOL's CLI installation process through a trusted channel, prefer a package manager or verified release, and inspect installer scripts before running them.

Risk: Write and destructive actions can modify or delete timeBuzzer activities.

Mitigation: Confirm the exact payload, target activity, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [timeBuzzer homepage](https://timebuzzer.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timebuzzer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions use live schemas and may return JSON data from the timeBuzzer connector.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
