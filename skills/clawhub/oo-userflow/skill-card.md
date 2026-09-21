## Description:

Userflow helps agents read, create, update, track, and delete Userflow users, groups, and events through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Userflow users, groups, and events through an OOMOL-connected account. It supports read, create-or-update, event tracking, and explicitly confirmed delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup instructions tell users to execute remote oo CLI installer scripts directly.

Mitigation: Review setup instructions before installing, prefer an official package-manager or manually reviewed installer flow, and do not run setup unless an auth or connection command fails.

Risk: Write and delete actions can change or remove Userflow records.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-userflow)
- [Userflow Homepage](https://userflow.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
