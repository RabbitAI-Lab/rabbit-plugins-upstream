## Description:

Theta EdgeCloud AI, GPU, video and game-character workflows: discover live services, run inference, manage approved resources, and verify costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeuslabsllc](https://clawhub.ai/user/zeuslabsllc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover Theta EdgeCloud services, run AI and media inference, manage approved GPU and application resources, and check usage and costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent character-session context update can run without the explicit approval gate used for comparable remote changes.

Mitigation: Require a patch or local policy enforcing confirm:true for theta.characters.session.context before allowing automated updates.

Risk: Credentials can authorize paid calls and remote resource changes; dry-run still permits reads.

Mitigation: Use least-privilege Theta credentials, provider-side quotas, THETA_DRY_RUN=1 before changes, and explicit approval for paid actions.

Risk: Prompts, uploaded file metadata, character messages and generated URLs may contain private data sent to Theta services.

Mitigation: Treat these inputs and outputs as private, avoid logging full responses, and do not publish customer inputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zeuslabsllc/skills/theta-edgecloud-skill)
- [Capability map and API contracts](references/capabilities.md)
- [Security scope](references/security.md)
- [Theta EdgeCloud hosted MCP server card](https://www.thetaedgecloud.com/.well-known/mcp/server-card.json)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live availability and pricing vary; approved paid actions can create ongoing costs.]

## Skill Version(s):

0.1.30 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
