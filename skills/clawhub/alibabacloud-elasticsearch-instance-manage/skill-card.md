## Description: <br>
Manages Alibaba Cloud Elasticsearch instance lifecycle, configuration, snapshots, analyzer dictionaries, Kibana settings, cluster YML settings, and plugins through Aliyun CLI guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operators and developers use this skill to generate Aliyun CLI workflows for administering Alibaba Cloud Elasticsearch instances, including lifecycle changes, configuration updates, snapshot and dictionary management, and plugin operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad Elasticsearch administration actions that affect service availability. <br>
Mitigation: Require explicit human approval before restarts, upgrades, YML changes, or custom plugin upload and installation. <br>
Risk: The skill can guide billing-impacting or credential-impacting actions. <br>
Mitigation: Require explicit human approval before billing conversion or password reset operations. <br>
Risk: Overbroad RAM permissions could allow unnecessary access across Elasticsearch resources. <br>
Mitigation: Use least-privilege RAM policies scoped to the exact instance and module instead of the full union policy unless required. <br>
Risk: Dictionary or plugin workflows can introduce unsafe external artifacts or storage exposure. <br>
Mitigation: Avoid public OSS buckets for dictionaries when a private service-role pattern is available, and do not run curl-to-shell installation commands blindly. <br>


## Reference(s): <br>
- [Elasticsearch Instance Management](references/instance-manage.md) <br>
- [Elasticsearch Config Management](references/config-manage.md) <br>
- [Elasticsearch Plugin Management](references/plugin-manage.md) <br>
- [RAM Policies](references/ram-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Aliyun CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Elasticsearch Node Specifications and Region Support](references/node-specifications-by-region.md) <br>
- [Alibaba Cloud Elasticsearch Product Page](https://www.aliyun.com/product/bigdata/elasticsearch) <br>
- [Alibaba Cloud Elasticsearch API Reference](https://next.api.aliyun.com/product/elasticsearch) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, markdown] <br>
**Output Format:** [Markdown with inline bash code blocks and Aliyun CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may include region, instance ID, idempotency token, timeouts, and per-command user-agent parameters.] <br>

## Skill Version(s): <br>
0.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
