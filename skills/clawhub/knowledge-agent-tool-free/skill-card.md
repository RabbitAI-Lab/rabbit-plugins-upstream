## Description: <br>
基于文件的知识组织工具，用于捕获、检索和整理 URL、视频、文章、论文摘要、社交帖子与研究笔记。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and agents use this skill to maintain a local Markdown knowledge base for saved links, extracted summaries, posts, research notes, tags, and searchable indexes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Add, tidy, and reindex operations can create or modify local Markdown knowledge-base files. <br>
Mitigation: Review or set KNOWLEDGE_DIR before use and review file changes after write-oriented commands. <br>
Risk: Sensitive or untrusted URLs and summaries may be stored locally as content and metadata. <br>
Mitigation: Avoid adding confidential sources unless local storage is approved, and review collected content before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/knowledge-agent-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notes, Markdown indexes, shell command examples, and JSON-style status responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local knowledge-base files under the configured KNOWLEDGE_DIR.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
