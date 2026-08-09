## Description: <br>
Predictalot helps agents call a self-hosted forecasting service for zero-shot time-series forecasts, ensembles, covariate-aware predictions, sample paths, and supervised tabular model training and prediction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to request forecasts from a predictalot instance they run or explicitly trust, including numeric time-series forecasts, covariate-conditioned forecasts, weighted ensembles, raw sample paths, and supervised tabular predictions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forecasting inputs, engineered features, and model identifiers are sent to the configured PREDICTALOT_URL. <br>
Mitigation: Point PREDICTALOT_URL only at a self-hosted or explicitly trusted endpoint, prefer HTTPS for remote access, and avoid sending sensitive data to untrusted services. <br>
Risk: A network-exposed predictalot service can be called by anyone who can reach it if authentication or network controls are weak. <br>
Mitigation: Use a strong bearer token, bind local deployments to loopback, and place any remote deployment behind TLS, a reverse proxy, VPN, or equivalent access control. <br>
Risk: Deleting a stored tabular model is irreversible. <br>
Mitigation: List models first, use only a modelId obtained in the current workflow, and require explicit user confirmation before issuing a delete request. <br>
Risk: The moirai-2 foundation model is documented as non-commercial. <br>
Mitigation: Do not use moirai-2 for commercial workloads unless the operator has confirmed the applicable terms permit that use; choose another supported model when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/predictalot) <br>
- [predictalot setup](references/setup.md) <br>
- [predictalot project homepage](https://github.com/psyb0t/docker-predictalot) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, API calls, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Consumer-only guidance for an already trusted predictalot service; outputs may include curl commands, MCP configuration, and confirmation prompts before destructive model deletion.] <br>

## Skill Version(s): <br>
1.1.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
