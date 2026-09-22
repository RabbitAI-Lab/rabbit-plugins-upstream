## Description:

Validate JSON syntax and structure using the Expanso Edge pipeline in CLI or MCP server modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aronchick](https://clawhub.ai/user/aronchick)

### License/Terms of Use:


## Use Case:

Developers and engineering agents use this skill to validate JSON strings or files locally, including API responses, pre-commit checks, CI/CD validation, and data-ingestion inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP mode exposes an unauthenticated JSON validation endpoint on all network interfaces by default.

Mitigation: Prefer CLI mode for local validation, or bind the MCP server to localhost with firewall and resource limits using a pinned, trusted expanso-edge version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aronchick/skills/expanso-json-validate)
- [Publisher profile](https://clawhub.ai/user/aronchick)
- [Expanso](https://expanso.io)
- [Hosted CLI pipeline](https://skills.expanso.io/json-validate/pipeline-cli.yaml)

## Skill Output:

**Output Type(s):** [json, text, shell commands, configuration]

**Output Format:** [JSON validation result with validity, error, parsed value, stats, and metadata fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI mode writes JSON to stdout; MCP mode returns a synchronous HTTP response with trace metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
