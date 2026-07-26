## Description: <br>
Content Swarm is a content-production SOP for topic planning, copywriting, cover creation, video scripting, quality review, and multi-platform distribution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaoshung1981888](https://clawhub.ai/user/gaoshung1981888) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operators and agents use this skill to plan, draft, package, review, and prepare social content for Xiaohongshu, WeChat Official Accounts, Douyin, Bilibili, and Kuaishou. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can create local task files under ~/.workbuddy/tasks. <br>
Mitigation: Require explicit user confirmation before filesystem writes and review the target paths before execution. <br>
Risk: The workflow prepares or initiates multi-platform public posting. <br>
Mitigation: Require human approval before any upload or publication, and review platform, title, tags, and content before posting. <br>
Risk: Broad trigger phrases may activate the workflow during general content requests. <br>
Mitigation: Narrow activation to the exact skill name or a dedicated command when installing or configuring the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gaoshung1981888/content-swarm) <br>
- [Publisher profile](https://clawhub.ai/user/gaoshung1981888) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with content drafts, task plans, platform-specific instructions, and shell command blocks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May prepare local task files and upload workflows; users should review content and confirm any public posting action.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
