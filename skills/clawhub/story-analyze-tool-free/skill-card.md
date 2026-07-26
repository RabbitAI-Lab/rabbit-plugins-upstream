## Description: <br>
长篇网文拆文分析工具免费版，面向网文作者与文学爱好者，用于提取章节大纲、分析故事节奏、梳理人物关系、追踪伏笔回收并导出分析报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External authors, writing analysts, and literary hobbyists use this skill to analyze long-form web novels for structure, pacing, character relationships, foreshadowing, and reader-reward moments. It can produce reports that help compare published works or improve a user's own writing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests read, write, and shell execution authority for analyzing local novel text and generating reports. <br>
Mitigation: Install and run it only in a controlled workspace, avoid sensitive files, and review proposed file reads, writes, and commands before execution. <br>
Risk: The artifact accepts output paths and an optional callback URL, which could direct generated content or notifications to an unintended location. <br>
Mitigation: Confirm every output path and callback URL before allowing execution, and prefer local report output unless remote delivery is explicitly needed. <br>
Risk: Analysis results may be incomplete or misleading because they depend on the agent's model capability and the quality of the source text. <br>
Mitigation: Treat generated pacing, relationship, foreshadowing, and writing recommendations as review aids and validate conclusions against the original novel text. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports and structured text, JSON, or CSV outputs depending on requested output_format.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact describes optional callback_url, configurable output paths, and command-driven report generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
