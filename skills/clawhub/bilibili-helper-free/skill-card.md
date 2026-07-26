## Description: <br>
Bilibili Helper Free helps Bilibili creators draft video titles, descriptions, tags, and spoken scripts for upload preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bilibili content creators and their agents use this skill to prepare upload-ready titles, descriptions, tags, and basic spoken scripts before publishing videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated titles, descriptions, tags, or scripts may be inaccurate, low quality, or misaligned with current Bilibili rules and recommendation behavior. <br>
Mitigation: Review generated posting text, titles, and tags before publishing, and check current platform guidance for sensitive or restricted topics. <br>
Risk: The artifact declares command execution and describes an optional local bili.sh workflow that is not necessary for ordinary drafting use. <br>
Mitigation: Only allow command execution when the local workflow is intentionally installed and trusted; otherwise use the skill for text drafting only. <br>
Risk: API key configuration examples could lead users to expose credentials if copied into shared files or version control. <br>
Mitigation: Store API keys in the local environment or a secrets manager and avoid committing credentials to repositories or shared logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bilibili-helper-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text or Markdown with optional shell command snippets and JSON-shaped examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated posting materials should be reviewed by the creator before use on Bilibili.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
