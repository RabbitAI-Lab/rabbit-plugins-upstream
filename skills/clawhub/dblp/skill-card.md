## Description: <br>
一个通过模型上下文协议（MCP）提供DBLP计算机科学文献数据库访问的服务，支持学术文献检索、引用生成及格式化功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External researchers, students, and developers use this skill to search computer science publication data, retrieve author or venue details, calculate result statistics, and collect BibTeX entries for export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawHub security summary marks the release suspicious because local credential handling is under-disclosed and the artifacts include inconsistent gaokao/XBY references. <br>
Mitigation: Use a throwaway or restricted API key, confirm that the unrelated references are acceptable before installation, and remove the local credential after use if persistence is not intended. <br>
Risk: The skill can write BibTeX export files to user-provided paths. <br>
Mitigation: Review the export destination before running the export workflow and avoid sensitive directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/dblp) <br>
- [XiaoBenYang API key portal](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration] <br>
**Output Format:** [Markdown or JSON-like tool results, with optional BibTeX file export] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a XiaoBenYang API key and can write BibTeX exports to a user-provided path.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
