## Description: <br>
Prove Before & After Act anchors an agent's reasoning before critical actions and records resulting proof data through xProof REST, MCP, and x402 workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonxkensei](https://clawhub.ai/user/jasonxkensei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add pre-action audit anchors, post-action proof records, verification lookups, certificates, badges, and payment-aware proof creation to autonomous agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an external service and creates blockchain-backed public proof or audit records. <br>
Mitigation: Use it only for workflows that intentionally require public proof records; hash content locally and avoid sensitive filenames, author labels, or metadata. <br>
Risk: API keys and x402 payments can authorize proof creation or autonomous spending. <br>
Mitigation: Protect API keys, keep them out of repositories, set strict spend limits, and require approval rules before enabling x402 in production. <br>
Risk: Webhook integrations can expose operational endpoints if configured loosely. <br>
Mitigation: Use HTTPS webhook targets, validate signatures, and verify the destination before processing callbacks. <br>


## Reference(s): <br>
- [Server-resolved source import](https://github.com/jasonxkensei/xProof/tree/main/clawhub-publish/xproof) <br>
- [xProof homepage](https://xproof.app) <br>
- [ClawHub skill listing](https://clawhub.ai/jasonxkensei/skills/xproof) <br>
- [API Reference](references/api-reference.md) <br>
- [Certification API](references/certification.md) <br>
- [MCP Server](references/mcp.md) <br>
- [x402 Payments](references/x402.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown] <br>
**Output Format:** [Markdown documentation with JSON request and response examples plus shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agents send SHA-256 hashes and optional metadata to REST or MCP endpoints; xProof returns proof identifiers, verification URLs, certificate links, and blockchain transaction metadata.] <br>

## Skill Version(s): <br>
4.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
