## Description: <br>
Call RouteMesh's unified JSON-RPC endpoint for any EVM chainId using a helper script to fetch onchain data, debug RPC responses, or demonstrate RouteMesh routing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kermankohli](https://clawhub.ai/user/kermankohli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to call RouteMesh's unified JSON-RPC endpoint for EVM chain data, inspect JSON-RPC responses, and test RouteMesh routing for a chain and method. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is incomplete because it asks agents to run a helper script that is not packaged. <br>
Mitigation: Review before installing and provide or verify the helper script before attempting execution. <br>
Risk: The skill uses a RouteMesh API key and allows a custom RPC base URL. <br>
Mitigation: Use a scoped ROUTEMESH_API_KEY, keep it out of logs and terminal output, and set --url only to endpoints you intentionally trust. <br>


## Reference(s): <br>
- [RouteMesh homepage](https://routeme.sh) <br>
- [RouteMesh unified RPC endpoint](https://lb.routeme.sh/rpc/{chainId}/{apiKey}) <br>
- [ClawHub skill page](https://clawhub.ai/kermankohli/skills/routemesh-crypto-rpc) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-RPC parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 or python and a ROUTEMESH_API_KEY for authenticated RouteMesh requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
