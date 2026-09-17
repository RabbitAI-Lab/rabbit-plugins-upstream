## Description:

Formaloo (formaloo.com). Use this skill for Formaloo requests involving reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Formaloo forms and submitted rows from an agent session, including listing, retrieving, creating, updating, and deleting Formaloo data after confirming write or destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup directs agents to remote installer scripts for the oo CLI.

Mitigation: Prefer a verified or package-manager installation of the oo CLI, and avoid running the remote installer pipeline directly unless the user has reviewed and approved it.

Risk: Formaloo write actions can create or update submitted data.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: The delete_row action permanently deletes submitted Formaloo rows.

Mitigation: Require explicit user approval for the target row before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-formaloo)
- [Formaloo Homepage](https://www.formaloo.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests and returns oo CLI JSON responses with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
