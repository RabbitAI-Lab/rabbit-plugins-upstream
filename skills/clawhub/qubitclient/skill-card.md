## Description: <br>
Unified quantum calibration analysis package that aggregates curve fitting and parameter extraction, neural network spectrum analysis, LLM-based calibration review, and MCP-based real-time measurement control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yaqiangsun](https://clawhub.ai/user/yaqiangsun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and quantum calibration engineers use this skill to install and configure qubitclient, initialize local configuration files, and call Python clients for calibration analysis, result review, and live measurement control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated configuration files can contain API keys, VLLM credentials, and license tokens. <br>
Mitigation: Keep qubitclient.json and .mcp.json out of version control and restrict access to credentials. <br>
Risk: MCP control features can change live measurement settings. <br>
Mitigation: Use control features only in authorized environments where live measurement changes are permitted and monitored. <br>
Risk: Package installation and client initialization depend on trusting the qubitclient package source. <br>
Mitigation: Verify the package source before installation and use an approved environment for deployment. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/yaqiangsun/QubitClient/tree/main/skills/qubitclient) <br>
- [Qubitclient ClawHub listing](https://clawhub.ai/yaqiangsun/skills/qubitclient) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with bash commands, JSON configuration examples, and Python code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes credential-bearing configuration examples that should be adapted locally.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
