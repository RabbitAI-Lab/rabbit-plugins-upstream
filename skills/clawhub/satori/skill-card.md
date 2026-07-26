## Description: <br>
Satori provides persistent long-term memory for continuity across AI sessions, providers, and code-generation tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[joelachance](https://clawhub.ai/user/joelachance) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI-tool users use Satori to save notable decisions, preferences, deadlines, and project context and retrieve them in later conversations across Claude Code, Cursor, Windsurf, or other terminal-capable AI tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store and reuse sensitive conversation details through an external Satori CLI and memory service. <br>
Mitigation: Configure the agent to ask before saving or searching memory, and avoid storing sensitive personal or business information unless explicitly intended. <br>
Risk: Stored memories and CLI credentials may persist beyond the current AI session. <br>
Mitigation: Verify how to inspect, delete, disable, and secure Satori memory records and CLI credentials before installation or deployment. <br>


## Reference(s): <br>
- [Fact Extraction Criteria](references/fact-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown/text with inline shell commands and JSON parsing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute Satori CLI commands that store or retrieve memory via an external service; search results are JSON for agent-side parsing.] <br>

## Skill Version(s): <br>
0.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
