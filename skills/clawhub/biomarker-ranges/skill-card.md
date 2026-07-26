## Description: <br>
基于Morgan Levine PhenoAge时钟模型，通过血液生物标志物计算生物年龄的服务。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to calculate biological age from blood biomarkers with the Morgan Levine PhenoAge clock and to retrieve reference ranges for supported PhenoAge biomarkers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A third-party API key is stored in a local plaintext .env file. <br>
Mitigation: Use a limited or revocable API key, restrict file access to the local workspace, and rotate the key if the workspace is shared or exposed. <br>
Risk: Biological-age inputs may contain sensitive health-related biomarker data sent to an external service. <br>
Mitigation: Confirm the receiving service, data retention expectations, and allowed remote calls before using real personal or clinical data. <br>
Risk: Security evidence reports unclear scope signals for this skill. <br>
Mitigation: Review the skill behavior and publisher documentation before deployment, especially the external API dependency and API-key handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/biomarker-ranges) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown summary of JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a third-party API key and sends biomarker inputs to an external API service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
