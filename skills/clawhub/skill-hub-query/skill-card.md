## Description: <br>
Query, install, update, and edit AI agent skills on compatible Skill Hub servers, using authenticated API access when a token is configured and public fallback access when it is not. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to search compatible skill hubs, inspect versions, install or update skills, diagnose hub configuration, and edit owned skill card metadata when a hub supports editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install agent skills and edit Hub metadata, including authenticated operations against private or compatible Hubs. <br>
Mitigation: Use least-privilege credentials, keep tokens in the documented config path with restrictive permissions, and require explicit approval before installs or metadata edits. <br>
Risk: Installing from an untrusted Hub can introduce unreviewed skills into an agent environment. <br>
Mitigation: Review and scan skills before installation, and use trusted or self-hosted Hubs for routine workflows. <br>
Risk: The security evidence notes an edit-backup cleanup path that does not safely constrain skill names. <br>
Mitigation: Avoid using edit.sh with slugs containing special characters until slug validation is added there. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-hub-query) <br>
- [README](README.md) <br>
- [Skill Hub API Reference](references/api.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with tables and inline bash commands; supporting scripts may emit text or JSON diagnostics.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local cache files, installed skill directories, credentials guidance, and edit backups.] <br>

## Skill Version(s): <br>
1.1.5 (source: server release metadata and CHANGELOG.md, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
