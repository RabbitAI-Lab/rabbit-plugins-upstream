## Description: <br>
predictalot helps an agent use a self-hosted forecasting service for zero-shot time-series forecasts, ensembles, MCP tools, and supervised tabular prediction through REST requests and setup guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to point an agent at a trusted predictalot service, run forecast and model-management requests, and interpret time-series or tabular prediction responses. It is useful when users need quantile bands, sample paths, covariate-aware forecasts, ensembles, or supervised tabular predictions from a self-hosted endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A network-exposed predictalot HTTP or MCP service can be called by anyone who can reach the port. <br>
Mitigation: Bind the service to localhost by default, expose it only through a trusted proxy or VPN, and require a strong bearer token for shared or remote access. <br>
Risk: Forecast and training requests send time series, engineered features, and model identifiers to the configured PREDICTALOT_URL. <br>
Mitigation: Point the skill only at a self-hosted or explicitly trusted endpoint, prefer HTTPS for remote use, and avoid sending sensitive proprietary data to untrusted services. <br>
Risk: Deleting a tabular model is irreversible. <br>
Mitigation: Only delete model IDs returned by the live model list or a train response, and require explicit user confirmation before issuing DELETE requests. <br>
Risk: One referenced foundation model, moirai-2, is described by the artifact as non-commercial. <br>
Mitigation: For commercial workflows, exclude moirai-2 and use models or ensembles with licenses suitable for the intended deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/predictalot) <br>
- [predictalot project homepage](https://github.com/psyb0t/docker-predictalot) <br>
- [Setup guide](artifact/references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON request bodies, endpoint descriptions, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl commands and example REST or MCP payloads for a configured PREDICTALOT_URL.] <br>

## Skill Version(s): <br>
1.1.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
