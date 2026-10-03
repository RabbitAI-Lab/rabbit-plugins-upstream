## Description:

Render (render.com). Use this skill for ANY Render request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Render accounts, workspaces, services, and deploys, and to run controlled service operations such as restart, resume, suspend, deploy trigger, and rollback through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger high-impact Render actions, including suspend and rollback.

Mitigation: Confirm the target service ID, payload, and expected effect with the user before write or destructive actions.

Risk: Fallback setup guidance includes remote CLI installer commands.

Mitigation: Review the OOMOL CLI installer source and prefer a verified or package-manager install path before use.

## Reference(s):

- [ClawHub Render Skill](https://clawhub.ai/oomol/skills/oo-render)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Render Homepage](https://render.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive Render actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
