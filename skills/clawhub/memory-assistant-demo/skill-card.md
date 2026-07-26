## Description: <br>
记忆助手 - 帮助用户管理、搜索和组织记忆文件。支持创建记忆条目、按日期或关键词搜索记忆、以及长期记忆的个性化更新。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Users and agents use this skill to create daily memory notes, search memory files by keyword or date, and consolidate long-term notes into MEMORY.md. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to create, append, search, or manually edit local memory files that can contain private or important notes. <br>
Mitigation: Confirm target paths and contents before writing or editing MEMORY.md or files under memory/, and review search results before sharing them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local memory file edits under memory/ and MEMORY.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
