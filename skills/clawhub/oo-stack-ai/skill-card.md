## Description:

StackAI lets agents operate StackAI through an OOMOL-connected account using the oo CLI connector to inspect schemas, run deployed flows, and fetch run metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run deployed StackAI flows and retrieve run metadata through an OOMOL-managed StackAI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running deployed StackAI flows can trigger configured flow behavior or consume credits.

Mitigation: Inspect the live schema, confirm the exact run_flow payload and intended effect with the user, and stop on billing errors before retrying.

Risk: The setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Use setup only after a matching CLI-missing or authentication failure, and prefer a verified installer, signed package, or reviewed script where possible.

Risk: Connector inputs and outputs depend on live OOMOL and StackAI action schemas.

Mitigation: Fetch the action schema before constructing payloads and avoid relying on stale assumptions about connector fields.

## Reference(s):

- [ClawHub StackAI skill page](https://clawhub.ai/oomol/skills/oo-stack-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [StackAI homepage](https://www.stack-ai.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI stack_ai connector and should fetch the live action schema before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
