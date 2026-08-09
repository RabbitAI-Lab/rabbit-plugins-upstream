## Description: <br>
Bailian Web Search helps agents call Alibaba Bailian/ModelStudio APIs for AI-optimized web search and concise, multi-source results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill when they need an agent to perform AI-assisted web search through Alibaba Bailian/ModelStudio and return concise synthesized results. It is not suitable for workflows that require fully deterministic or independently verified answers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is described as a web-search helper but requests broad local file and shell capabilities. <br>
Mitigation: Install and run it in a sandbox, disable exec/write where possible, and review proposed commands before execution. <br>
Risk: Search prompts and context may be sent to an external Bailian/ModelStudio API. <br>
Mitigation: Use a limited API key and avoid sensitive search terms, private files, personal data, or confidential business context. <br>
Risk: AI-optimized search results may be incomplete, stale, or unsuitable for critical deterministic decisions. <br>
Mitigation: Verify important claims against primary sources before using results for decisions with legal, financial, safety, or operational impact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bailian-web-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-style result examples and shell environment configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an API key; artifact evidence declares broad read, exec, write, and glob tool access.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
