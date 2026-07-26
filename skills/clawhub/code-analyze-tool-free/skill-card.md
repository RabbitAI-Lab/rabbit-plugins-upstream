## Description: <br>
code-analyze-tool-free provides a Markdown-driven framework for structured analysis of code, data, text, decisions, and visualizations with priorities, source labels, counterarguments, and action recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual engineers use this skill to structure code reviews, technical decisions, data summaries, and comparison reports into prioritized findings, source-labeled reasoning, counterevidence, and action recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims local/offline privacy, but server security review says that claim is unreliable unless the agent uses a truly local model. <br>
Mitigation: Review before using private code, business data, or regulated content, and confirm the configured agent and model keep data local. <br>
Risk: The skill requests broad read, exec, write, glob, and grep capability without clear limits. <br>
Mitigation: Require explicit approval before shell commands, network callbacks, or file writes, and scope file access to the project being analyzed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-analyze-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown analysis reports with optional inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request input text, code, data, and optional analysis settings; shell commands, callbacks, and file writes should require explicit approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
