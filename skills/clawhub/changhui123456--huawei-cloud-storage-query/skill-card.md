## Description: <br>
Queries Huawei Cloud storage resources across EVS, OBS, SFS Turbo, and CBR using packaged read-only Python scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud disks, object storage buckets, file systems, and backup resources. It helps gather live resource details for inventory, troubleshooting, and configuration planning without creating, modifying, or deleting cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Huawei Cloud credentials to query account resources. <br>
Mitigation: Use least-privilege read-only Huawei Cloud credentials and avoid exposing credential environment variables in prompts, logs, or returned output. <br>
Risk: The security evidence reports that TLS certificate verification is disabled. <br>
Mitigation: Review before installing and prefer a version that keeps TLS certificate verification enabled. <br>
Risk: The environment setup installs runtime Python dependencies. <br>
Mitigation: Review setup behavior before running it on sensitive hosts and prefer pinned, reviewed dependencies. <br>


## Reference(s): <br>
- [EVS Python Script Usage Guide](artifact/references/evs/guide.md) <br>
- [OBS Python Script Usage Guide](artifact/references/obs/guide.md) <br>
- [SFS Python Script Usage Guide](artifact/references/sfs/guide.md) <br>
- [CBR Python Script Usage Guide](artifact/references/cbr/guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON query results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query output depends on Huawei Cloud API responses and the selected service script.] <br>

## Skill Version(s): <br>
9.9.100 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
