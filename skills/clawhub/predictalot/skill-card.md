## Description: <br>
predictalot helps agents use a trusted self-hosted forecasting service for zero-shot time-series forecasts, ensembles, and supervised tabular predictions through REST, MCP, curl examples, and setup guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to connect an agent to a trusted predictalot instance, forecast numeric time series with supported foundation models, build ensembles, and train or query supervised tabular prediction models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forecast, training, feature, and model identifier data are sent to the configured PREDICTALOT_URL. <br>
Mitigation: Point the skill only at a predictalot server you run or explicitly trust, prefer HTTPS for remote access, and treat submitted time series and features as sensitive. <br>
Risk: A reachable unauthenticated or weakly protected service can accept forecast, training, MCP, and model-management calls. <br>
Mitigation: Bind the service to loopback by default, set strong bearer tokens before any shared exposure, and place remote deployments behind a reverse proxy or VPN. <br>
Risk: Deleting a tabular model permanently removes the stored model. <br>
Mitigation: Confirm the target modelId with the user before deletion and use identifiers discovered from a recent model listing or train response. <br>
Risk: The moirai-2 model is documented as non-commercial and may be unsuitable for commercial workflows. <br>
Mitigation: Avoid moirai-2 in commercial use, or set its ensemble weight to zero and use the documented Apache-licensed alternatives where appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/predictalot) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [predictalot setup](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-predictalot) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, HTTP request examples, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are proposals and examples for a configured predictalot server; forecast responses depend on the remote service and selected model.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
