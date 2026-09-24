## Description:

Convert XML input into JSON format using Expanso Edge pipelines for CLI, MCP server, or cloud deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aronchick](https://clawhub.ai/user/aronchick)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to convert XML payloads into JSON through a local Expanso Edge CLI pipeline, an MCP-style HTTP pipeline, or Expanso Cloud deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP mode starts an unauthenticated network service on all interfaces by default.

Mitigation: Prefer the CLI pipeline for local conversion, or bind the MCP listener to localhost and add authentication, request-size limits, and rate limits before network exposure.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/aronchick/skills/expanso-xml-to-json)
- [README](artifact/README.md)
- [Skill Usage](artifact/SKILL.md)
- [Skill Metadata](artifact/skill.yaml)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON object with json, valid, error, and metadata fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI mode writes JSON to stdout; MCP mode returns a synchronous HTTP response.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact skill.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
