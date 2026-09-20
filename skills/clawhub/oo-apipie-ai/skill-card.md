## Description:

APIpie AI (apipie.ai) skill for running chat completion, embedding, and model-listing actions through the OOMOL apipie_ai connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect APIpie AI action schemas and run OOMOL connector actions for chat completions, embeddings, and model listings through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute arbitrary code if followed without verification.

Mitigation: Review the oo CLI installation path and prefer documented package-manager or manually verified installation steps before installing.

Risk: Write or billable APIpie AI actions may create embeddings, consume credits, or otherwise affect the connected account.

Mitigation: Inspect the live action schema and confirm the exact payload and effect before running write or billable operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-apipie-ai)
- [APIpie AI Homepage](https://apipie.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [APIpie AI Connection Setup](https://console.oomol.com/app-connections?provider=apipie_ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
