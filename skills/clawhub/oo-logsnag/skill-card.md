## Description:

LogSnag (logsnag.com). Use this skill for ANY LogSnag request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate LogSnag through an OOMOL-connected account, inspecting live connector schemas and running user, event, and insight actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing LogSnag actions can mutate user profiles, events, or insights if run without confirmation.

Mitigation: Confirm the exact action, payload, and expected effect before identify_user, mutate_insight, publish_event, or publish_insight; inspect the live connector schema before constructing the payload.

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Prefer a signed or package-manager installation path; otherwise independently verify the OOMOL installer source before execution.

Risk: Connector execution depends on an authenticated OOMOL account, an active LogSnag connection, and sufficient billing state.

Mitigation: Run login, connection, or billing recovery steps only after the corresponding command failure indicates they are required.

## Reference(s):

- [ClawHub LogSnag skill page](https://clawhub.ai/oomol/skills/oo-logsnag)
- [LogSnag homepage](https://logsnag.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; state-changing LogSnag actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
