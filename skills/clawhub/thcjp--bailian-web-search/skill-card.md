## Description: <br>
Bailian Web Search helps an agent call the Alibaba Bailian/ModelStudio web search API and return concise, multi-source search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users can use this skill when they need AI-assisted web search through Alibaba Bailian/ModelStudio for chat, agent orchestration, or LLM application workflows. It is not appropriate for decisions that require fully deterministic or independently verified answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to an external Alibaba Bailian/ModelStudio service. <br>
Mitigation: Do not submit secrets, credentials, private documents, or sensitive business data unless the provider and API key configuration have been intentionally approved. <br>
Risk: Search responses may be incomplete, outdated, or unsuitable for deterministic decisions. <br>
Mitigation: Use the results as research assistance and independently verify important facts before acting on them. <br>
Risk: The skill documentation gives a vague data-sharing notice and scope. <br>
Mitigation: Review data handling expectations and service terms before deployment in sensitive or regulated workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bailian-web-search) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped result examples and shell configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include concise search summaries, structured result data, error guidance, and API key configuration instructions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
