## Description: <br>
Queries Huawei Cloud EVS, OBS, SFS, and CBR storage resources through read-only local scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operators and developers use this skill to inspect Huawei Cloud storage inventories, metadata, quotas, policies, access settings, and backup details. It is intended for read-only discovery and verification tasks, not resource creation or modification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Huawei Cloud AK/SK credentials and queries live tenant data. <br>
Mitigation: Use least-privilege read-only credentials and avoid exposing credential environment variables or sensitive query results. <br>
Risk: Setup and runtime behavior may install network dependencies. <br>
Mitigation: Review dependency installation behavior and run the setup step only in an approved environment. <br>
Risk: The security summary flags disabled TLS verification and a get-pip fallback. <br>
Mitigation: Review or patch TLS verification and the get-pip fallback before use in sensitive environments. <br>
Risk: Queries may print sensitive project, ACL, LDAP, backup, and agent metadata. <br>
Mitigation: Limit query scope, handle output as sensitive tenant data, and cache or share results only where appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-storage-query) <br>
- [Publisher profile](https://clawhub.ai/user/huaweiclouddev) <br>
- [EVS Python Script Usage Guide](references/evs/guide.md) <br>
- [OBS Python Script Usage Guide](references/obs/guide.md) <br>
- [SFS Python Script Usage Guide](references/sfs/guide.md) <br>
- [CBR Python Script Usage Guide](references/cbr/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON query output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on live Huawei Cloud credentials, region, project scope, and the selected service guide.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
