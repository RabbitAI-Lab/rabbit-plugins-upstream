## Description:

Enables an agent to read, create, update, complete, clone, and delete Onfleet tasks through the OOMOL-connected oo CLI instead of direct Onfleet API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Onfleet task workflows from an agent session, including schema inspection and task list, retrieval, create, update, clone, completion, and deletion actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly.

Mitigation: Review the installer path before use and prefer a verified, pinned, or package-manager-based oo CLI installation method when available.

Risk: Write and destructive actions can change or delete Onfleet task data.

Mitigation: Confirm the exact payload and effect before write actions, and require explicit approval before destructive deletion actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onfleet)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Onfleet homepage](https://onfleet.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON responses, Operational guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and a connected Onfleet account before actions can run.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
