## Description: <br>
Provides web search and content extraction through the Brave Search API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to ask an agent for web search, information retrieval, and content extraction through Brave Search API workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says this Brave Search skill asks for broad command execution authority that is not clearly needed or bounded for search. <br>
Mitigation: Review the skill carefully before installing, run it only in a constrained environment, and prefer a version that limits itself to Brave Search API calls. <br>
Risk: Search queries, local files, or API keys could expose sensitive information when used with file-reading tools or raw command execution. <br>
Mitigation: Keep API keys scoped, configure them through environment variables, avoid sending sensitive queries or files, and remove secrets from logs and outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/brave-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key; outputs may include search results, extracted content, and setup guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
