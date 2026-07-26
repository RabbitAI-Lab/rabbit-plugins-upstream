## Description: <br>
Scaffolds a local Node.js workflow to fetch and parse event logs from EVM smart contracts using RPC, verified or user-provided ABI, and event selection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lkkchen](https://clawhub.ai/user/lkkchen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and blockchain engineers use this skill to scaffold a local project, obtain or provide a contract ABI, choose events, and fetch raw EVM logs into parsed text and JSON files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scaffolded workflow creates local project files and installs npm dependencies. <br>
Mitigation: Run it in a project directory you control and review generated files before executing the fetch and parse scripts. <br>
Risk: The workflow calls public ABI services or user-configured RPC endpoints and may use an Etherscan API key for ABI lookup. <br>
Mitigation: Use trusted RPC URLs and only provide an Etherscan API key when that use is acceptable for the environment. <br>
Risk: Fetched contract logs are written to local output files. <br>
Mitigation: Store outputs in an appropriate workspace and handle log data according to the project's data-retention and sharing requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lkkchen/skills/fetch-evm-logs) <br>
- [reference.md](artifact/reference.md) <br>
- [examples.md](artifact/examples.md) <br>
- [Sourcify contract repository](https://repo.sourcify.dev/) <br>
- [Sourcify API](https://sourcify.dev/server/) <br>
- [Etherscan API v2](https://api.etherscan.io/v2/api) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration, text, json] <br>
**Output Format:** [Markdown guidance with shell commands and generated project files that write logs.txt and logs.json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local project files, installs npm dependencies, calls configured RPC and ABI lookup services, and stores fetched logs under output/{address}_{chainId}/.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
