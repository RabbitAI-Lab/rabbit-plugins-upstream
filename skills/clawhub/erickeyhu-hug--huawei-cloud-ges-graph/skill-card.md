## Description: <br>
Provides terminal-oriented guidance and Python/Node.js scripts for operating Huawei Cloud Graph Engine Service (GES), including Cypher and GQL queries, schema and label management, graph editing, summary queries, and import/export workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to configure credentials and operate Huawei Cloud GES graph databases from an agent terminal using packaged Python or Node.js helpers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact operations such as graph deletion, export, import, and storage actions against a real Huawei Cloud GES environment. <br>
Mitigation: Use least-privilege credentials, avoid production credentials unless necessary, and require explicit human confirmation before delete, clear, export, import, or storage actions. <br>
Risk: The release evidence reports insecure TLS verification settings. <br>
Mitigation: Review or patch TLS verification settings before deploying the skill. <br>
Risk: Credential misuse or exposure could affect a live cloud environment. <br>
Mitigation: Do not print AK/SK, passwords, or tokens, and configure only credentials scoped to the intended graph operations. <br>


## Reference(s): <br>
- [Huawei Cloud GES graph data format documentation](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html) <br>
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html) <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ges-graph) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with inline Python, Node.js, shell commands, and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute live Huawei Cloud GES operations when configured with valid credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
