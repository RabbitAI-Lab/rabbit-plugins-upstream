## Description:

Converts JSON input into YAML output using Expanso Edge CLI or MCP pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aronchick](https://clawhub.ai/user/aronchick)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to convert JSON strings into YAML output from local CLI workflows or an MCP-style HTTP pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server and cloud deployment options expose more operational risk than local JSON-to-YAML conversion requires.

Mitigation: Prefer the local CLI pipeline when possible; if using the MCP server, bind it to localhost or protect it with network controls.

Risk: Remote cloud deployment by URL can make the exact pipeline content harder to verify before use.

Mitigation: Avoid deploying from the remote URL unless the pipeline content or digest has been verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aronchick/skills/expanso-json-to-yaml)
- [Expanso Cloud pipeline](https://skills.expanso.io/json-to-yaml/pipeline-cli.yaml)

## Skill Output:

**Output Type(s):** [text, configuration]

**Output Format:** [JSON object containing YAML text, validity status, error text, and metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts JSON text input; the CLI pipeline reads stdin and the MCP pipeline accepts POST requests to /convert.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
