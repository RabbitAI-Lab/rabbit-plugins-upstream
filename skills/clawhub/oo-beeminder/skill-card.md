## Description:

Use this skill to read, create, update, and delete Beeminder data through an OOMOL-connected Beeminder account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Beeminder goals and datapoints through the OOMOL oo CLI, including reading user and goal data and performing confirmed write or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends remote installer commands that execute code on the user's machine.

Mitigation: Review and verify the installer source before use; prefer a pinned, verified, or package-manager installation path for the oo CLI.

Risk: Beeminder write actions can create or update datapoints, and the delete action removes datapoints.

Mitigation: Confirm the exact action, target goal or datapoint, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-beeminder)
- [Beeminder Homepage](https://www.beeminder.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
