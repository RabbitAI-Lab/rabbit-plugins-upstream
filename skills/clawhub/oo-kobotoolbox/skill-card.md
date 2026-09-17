## Description:

KoboToolbox helps agents read, create, update, deploy, export, validate, and delete KoboToolbox projects and submissions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to manage KoboToolbox survey projects and submissions from an agent session after their OOMOL account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from OOMOL delivery endpoints without local verification.

Mitigation: Install the oo CLI only from a trusted, verified, pinned, or package-manager source, and review installer contents before execution.

Risk: Write and destructive actions can change KoboToolbox state or permanently delete submissions.

Mitigation: Confirm the exact payload, target project or submission, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub KoboToolbox Skill Page](https://clawhub.ai/oomol/skills/oo-kobotoolbox)
- [KoboToolbox Homepage](https://www.kobotoolbox.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
