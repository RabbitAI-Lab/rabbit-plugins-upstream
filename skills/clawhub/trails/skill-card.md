## Description: <br>
Integrates Trails cross-chain infrastructure through Widget, Headless SDK, or Direct API guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jameslawton](https://clawhub.ai/user/jameslawton) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to integrate Trails cross-chain payments, swaps, bridging, DeFi funding, and destination smart contract execution into React, Next.js, backend, or agent-driven applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may search project files and environment variables for Trails API keys, which can expose or mishandle secrets if the agent has broad access. <br>
Mitigation: Limit the agent to Trails-specific environment variables and avoid exposing privileged server keys in browser or client-side code. <br>
Risk: Generated payment, swap, bridge, calldata, batch settlement, or execute examples can move real funds or call destination contracts. <br>
Mitigation: Manually review every generated transaction path and contract call before signing or deployment, and test calldata flows on testnets first. <br>
Risk: The artifact recommends installing latest package versions, which can reduce reproducibility and supply-chain control. <br>
Mitigation: Pin package versions and commit lockfiles before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jameslawton/skills/trails) <br>
- [Trails documentation](https://docs.trails.build) <br>
- [Trails Docs MCP](https://docs.trails.build/mcp) <br>
- [Trails API reference](https://docs.trails.build/api) <br>
- [Trails SDK reference](https://docs.trails.build/sdk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, configuration snippets, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API calls or transaction-building examples that require manual review before signing or deployment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
