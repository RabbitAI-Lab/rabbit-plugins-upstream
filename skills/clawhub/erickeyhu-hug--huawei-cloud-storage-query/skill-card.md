## Description: <br>
Queries Huawei Cloud storage resources across EVS, OBS, SFS Turbo, and CBR using bundled read-only Python query scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud storage inventory, configuration, quotas, tags, backups, policies, and related identifiers without creating, modifying, or deleting resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup path disables TLS verification and may install remote Python packages while cloud credentials are present. <br>
Mitigation: Review the setup path before use, install in a disposable or controlled environment, and use least-privilege read-only Huawei Cloud credentials. <br>
Risk: Query results can expose Huawei Cloud storage, backup, bucket, and account inventory details. <br>
Mitigation: Run the skill only where that inventory output is appropriate, avoid sharing raw outputs broadly, and scope large queries by region, project, name, status, tag, or resource ID. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-storage-query) <br>
- [CBR Python Script Usage Guide](references/cbr/guide.md) <br>
- [EVS Python Script Usage Guide](references/evs/guide.md) <br>
- [OBS Python Script Usage Guide](references/obs/guide.md) <br>
- [SFS Python Script Usage Guide](references/sfs/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with skill action command invocations and JSON query results from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query outputs may include Huawei Cloud storage and account inventory details; large result sets should be scoped or cached.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
