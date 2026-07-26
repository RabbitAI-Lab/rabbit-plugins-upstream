## Description: <br>
谷歌搜索(免费版) helps agents run lightweight Google searches through browser automation, parse result titles, URLs, and snippets, filter results, and export structured search outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill for lightweight information retrieval, SEO keyword checks, learning references, and research collection when they need Google search results without a Google API key. It is not intended for black-hat SEO workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation sends search queries to Google and may expose sensitive terms or trigger search-provider anti-automation controls. <br>
Mitigation: Use non-sensitive queries, comply with applicable service terms, and run the skill only in environments where browser automation and outbound Google traffic are acceptable. <br>
Risk: The setup guidance includes a curl-to-bash Bun installer path without verification. <br>
Mitigation: Prefer an already-installed Node.js runtime or a verified package-manager installation route; only use remote shell installers after independent trust and integrity checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/free-google-search-tool-free) <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline Python, shell, and JSON examples; generated search results may be exported as JSON, Markdown, CSV, or text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include search status, result records with title, URL, snippet, and position, and optional execution logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
