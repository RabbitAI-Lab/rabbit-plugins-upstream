## Description:

Use this skill for Render requests involving reading, creating, updating, and deleting data on render.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Render accounts, services, workspaces, and deploys, and to run Render service operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags unsafe first-time installer guidance that pipes remote install scripts into a shell or PowerShell evaluator.

Mitigation: Review the installer source independently before running install commands, and prefer trusted package or manual installation paths when available.

Risk: The skill can perform Render state-changing operations, including restart, resume, suspend, deploy trigger, and rollback.

Mitigation: Require explicit user confirmation of the exact service, action, payload, and expected effect before running write, destructive, or suspension operations.

Risk: The security evidence notes that suspend_service is not labeled consistently with its service-impacting behavior.

Mitigation: Treat suspend_service as a state-changing operation requiring confirmation even if the artifact does not tag it as write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-render)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Render Homepage](https://render.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce command output summaries from Render connector calls; state-changing actions should include the target payload and expected effect for confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
