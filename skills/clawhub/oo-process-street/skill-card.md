## Description:

Operate Process Street through the OOMOL-connected oo CLI to read, create, and update workflows, workflow runs, tasks, and form fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Process Street workflows from an agent, including listing workflows and runs, creating workflow runs, updating task status, and editing workflow run form fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute arbitrary code if followed without verification.

Mitigation: Install the oo CLI only from a verified release or trusted package manager, and use checksum or signature verification when available.

Risk: Process Street workflow data and actions are routed through OOMOL's connector service.

Mitigation: Connect Process Street only after confirming that this routing is acceptable for the user's data handling and service policies.

Risk: Write actions can create workflow runs or modify tasks and form fields.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [Process Street homepage](https://www.process.st/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-process-street)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action-schema inspection before constructing Process Street write payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
