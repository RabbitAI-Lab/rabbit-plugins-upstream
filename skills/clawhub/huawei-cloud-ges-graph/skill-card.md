## Description: <br>
Provides access guidance and local Python/Node.js helpers for operating Huawei Cloud Graph Engine Service databases with Cypher, GQL, schema, label, summary, import/export, and graph editing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to query and manage Huawei Cloud GES graph databases from an agent-assisted terminal workflow. It supports graph reads, schema-aware edits, imports, exports, and object-storage transfer helpers when configured with Huawei Cloud credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses powerful Huawei Cloud credentials and can operate on real graph data. <br>
Mitigation: Use a non-production or least-privilege Huawei Cloud project, avoid long-lived credentials in the skill directory, and rotate credentials after testing. <br>
Risk: Transport verification is disabled in the included Python and Node.js helpers. <br>
Mitigation: Enable certificate verification and use trusted HTTPS endpoints before using real credentials or sensitive graph data. <br>
Risk: Graph clear, delete, import, export, and OBS object operations can destroy, expose, or overwrite data. <br>
Mitigation: Require explicit user confirmation, verify target graph and bucket paths, and take backups before destructive or file-transfer operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ges-graph) <br>
- [Huawei Cloud GES graph data format](https://support.huaweicloud.com/usermanual-ges/ges_01_0153.html) <br>
- [Huawei Cloud GES business API access guide](https://support.huaweicloud.com/api-ges/ges_03_0112.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline Python, Node.js, shell commands, and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud GES connection settings and credentials supplied by environment variables or local configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, target metadata, scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
