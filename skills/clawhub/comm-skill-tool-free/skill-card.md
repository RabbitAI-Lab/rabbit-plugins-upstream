## Description: <br>
Helps an agent draft context-aware, empathetic messages from conversation history, emotional cues, relationship context, and communication channel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and lightweight agent users use this skill to draft emails, messages, and difficult-conversation replies with structured, empathetic framing. It supports tone adjustment, emotional subtext review, and communication templates, but the user should review any draft before sending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad command execution, file reading/searching, callbacks, and possible network/API access while handling sensitive communication content. <br>
Mitigation: Use it only in an agent environment where those capabilities can be disabled or approved per action, and avoid confidential emails, customer complaints, credentials, or private conversation history unless the host agent and API provider are acceptable for that data. <br>
Risk: Security evidence flags inconsistent privacy claims about whether sensitive messages stay local. <br>
Mitigation: Review the skill before installation, verify the host agent and configured API provider data handling, and manually review generated drafts before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/comm-skill-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or structured JSON-style responses with draft text, status, result data, and execution logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional settings such as tone, channel, relationship, framework, retry behavior, cache behavior, timeout, and output format.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
