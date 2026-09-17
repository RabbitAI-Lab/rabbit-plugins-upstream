## Description:

Render (render.com) helps agents read and manage Render account resources through the OOMOL Render connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Render users, services, workspaces, and deploys, and to manage service lifecycle actions such as deploy, restart, resume, suspend, and rollback through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Review the installer source or use a trusted package or installation path before running setup commands.

Risk: The skill can trigger deploys, restarts, resumes, suspension, and rollbacks for Render services.

Mitigation: Inspect the live action schema and require explicit user confirmation of the target service, payload, and expected effect before any state-changing action.

Risk: Security evidence notes that one service-suspending action is documented as if it were read-only.

Mitigation: Treat service suspension as a state-changing action and require explicit confirmation before execution.

## Reference(s):

- [Render homepage](https://render.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Render skill](https://clawhub.ai/oomol/skills/oo-render)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Render connector JSON responses with execution IDs.]

## Skill Version(s):

1.0.3 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
