## Description:

Helps a person inspect what ~alter has inferred about them, review the evidence and rules behind those readings, manage who may make competence claims, and contest readings they believe are wrong.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their agents use this skill to review their own ~alter identity record, understand trait movement and evidence trails, manage attestations and consent, and append contests when a reading is disputed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to the user's own ~alter identity records through an existing member key.

Mitigation: Install it only when the agent should use that member key, and review ~alter consent settings and connected sources before use.

Risk: Contestations or attestation changes may be stored in the user's identity log.

Mitigation: Review the requested action and affected reading or attestation before asking the agent to make changes.

Risk: Using a noncanonical endpoint could expose credentials or identity data to an unintended service.

Mitigation: Configure the MCP server only at https://mcp.truealter.com/api/v1/mcp.

## Reference(s):

- [~alter hosted MCP endpoint](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill listing](https://clawhub.ai/true-alter/skills/alter-know-yourself)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown guidance with MCP tool names and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ALTER_API_KEY for the ~alter hosted MCP server.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
