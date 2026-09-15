## Description:

Enables agents to read, create, comment on, and update Pivotal Tracker work items through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to inspect Pivotal Tracker projects and stories, then create stories, add comments, or update story state after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running mutable remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation source first, prefer a pinned package or installer with checksum or signature verification, and avoid running installer commands from an elevated shell.

Risk: Story creation, comments, and state updates can change Pivotal Tracker data.

Mitigation: Confirm the exact project, story, action, and JSON payload with the user before executing any write action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pivotal-tracker)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Pivotal Tracker homepage](https://www.pivotaltracker.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
