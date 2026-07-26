## Description: <br>
SeekDB routes agents to installation, local deployment, and source-build guidance for a lightweight OceanBase-compatible database. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oceanbase](https://clawhub.ai/user/oceanbase) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to install, deploy, verify, troubleshoot, and build SeekDB across supported local, container, embedded Python, and source-build workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged installation and service-management commands can change package sources, enable persistent services, or expose local database ports. <br>
Mitigation: Review each command before execution and require explicit confirmation before sudo, systemd, Windows Administrator, or service changes. <br>
Risk: The APT flow uses a '[trusted=yes]' repository configuration. <br>
Mitigation: Prefer a signed HTTPS repository or offline package; avoid the trusted repository path unless the user explicitly accepts it after review. <br>
Risk: Cleanup and uninstall flows can remove SeekDB data directories. <br>
Mitigation: Back up data and confirm exact paths before running cleanup scripts or recursive removal commands. <br>
Risk: Some install paths download remote packages or scripts, including an alternative installer that runs with root privileges. <br>
Mitigation: Use documented package-manager methods when available, download only from the cited sources, and inspect scripts before execution. <br>


## Reference(s): <br>
- [SeekDB product documentation](https://www.oceanbase.ai/docs/seekdb-overview/) <br>
- [SeekDB software download center](https://mirrors.oceanbase.com/oceanbase/community/stable/) <br>
- [Deploy SeekDB by systemd](https://docs.seekdb.ai/seekdb/deploy-by-systemd/) <br>
- [pyseekdb embedded install](https://docs.seekdb.ai/seekdb/pyseekdb-sdk-get-started/#install-pyseekdb) <br>
- [SeekDB Docker image README](https://github.com/oceanbase/docker-images/blob/main/seekdb/README.md) <br>
- [Install skill](artifact/install/SKILL.md) <br>
- [Build skill](artifact/build/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code blocks, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single conversational stream; includes platform-specific command sequences and generated scripts.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
