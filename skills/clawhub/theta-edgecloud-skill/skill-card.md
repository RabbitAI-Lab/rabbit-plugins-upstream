## Description:

Theta EdgeCloud AI, GPU, video and game-character workflows: discover live services, run inference, manage approved resources, and verify costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zeuslabsllc](https://clawhub.ai/user/zeuslabsllc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to discover Theta EdgeCloud services, run bounded inference, manage approved GPU and dedicated-serving resources, and work with Theta video and AI Characters APIs using protected credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make paid or mutating Theta API calls when credentials permit.

Mitigation: Use least-privilege Theta credentials, keep THETA_DRY_RUN=1 until a specific action is approved, and require explicit scope and spending approval for paid writes.

Risk: Provider responses and outputs can include private user content, signed media URLs, or other sensitive data.

Mitigation: Treat outputs as private and untrusted, avoid logging complete provider responses, and do not publish customer inputs or presigned URLs.

Risk: Post-call accounting and cleanup checks cannot guarantee provider-side spend caps or deletion after ambiguous timeouts.

Mitigation: Use provider-side quotas, reconcile remote jobs or resources after ambiguous outcomes, and manually verify cleanup before reporting success.

## Reference(s):

- [Capability map and verified API contracts](references/capabilities.md)
- [Security scope](references/security.md)
- [Theta EdgeCloud GPU deployment announcement](https://blog.thetatoken.org/ai-agents-can-now-deploy-edgecloud-gpus-themselves/)
- [Theta AI Characters OpenAPI reference](https://github.com/thetatoken/theta-edge-cloud-ai-characters-public/blob/main/reference/ai-characters-openapi.json)
- [Theta deployment API key documentation](https://docs.thetatoken.org/docs/use-edgecloud-api-keys-to-manage-deployments)
- [Theta on-demand API MCP source](https://github.com/thetatoken/on-demand-api-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and command snippets, plus structured runtime command results when invoked.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Theta service metadata, inference outputs, resource identifiers, usage data, and redacted errors.]

## Skill Version(s):

0.1.28 (source: package.json, README, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
