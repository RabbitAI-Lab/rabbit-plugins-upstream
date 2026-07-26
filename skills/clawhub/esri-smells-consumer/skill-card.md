## Description: <br>
Paid client skill for calling the Esri Workflow Smell Detector x402 endpoint on Base/USDC to scan an ArcGIS Pro project snapshot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danmaps](https://clawhub.ai/user/danmaps) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and GIS automation engineers use this skill to submit ArcGIS Pro project snapshots to a paid preflight smell detector before deciding whether and how to automate ArcPy, geoprocessing, or AGOL workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a wallet private key and wallet address to authorize x402 payments. <br>
Mitigation: Use a dedicated low-balance wallet, keep the private key out of shell history and logs, and remove the environment variables after use. <br>
Risk: The helper can authorize a paid request after receiving an HTTP 402 challenge. <br>
Mitigation: Require the agent to show the exact cost, endpoint, network, and payment recipient before making any paid call. <br>
Risk: A changed or incorrect endpoint could affect both payment and data destination. <br>
Mitigation: Verify the endpoint is https://api.x402layer.cc/e/esri-smells before sending snapshots or payment authorization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/danmaps/skills/esri-smells-consumer) <br>
- [Publisher profile](https://clawhub.ai/user/danmaps) <br>
- [Esri Smell Detector endpoint](https://api.x402layer.cc/e/esri-smells) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Endpoint responses include summary, risk_score, issues, flags, version, and requestHash.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
