## Description: <br>
Build original LangGraph agents for Warden Protocol and prepare them for publishing in Warden Studio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kulotzkih](https://clawhub.ai/user/kulotzkih) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to create original Warden Protocol LangGraph agents, scaffold TypeScript or Python projects, test API endpoints, and prepare deployments for Warden Studio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The initializer writes a new agent project with dependencies and environment templates into the selected workspace. <br>
Mitigation: Run it only in the intended workspace and review generated dependencies and files before installing or deploying them. <br>
Risk: Example configuration files reference API keys and database credentials that are placeholders. <br>
Mitigation: Keep real API keys out of source control and replace example database credentials before any non-local deployment. <br>
Risk: Agent testing sends requests to user-supplied endpoints and may include authentication headers. <br>
Mitigation: Test only endpoints you trust and avoid exposing sensitive prompts, wallet data, account data, or raw secrets in logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kulotzkih/skills/lex) <br>
- [Warden Protocol documentation](https://docs.wardenprotocol.org) <br>
- [Warden community agents](https://github.com/warden-protocol/community-agents) <br>
- [LangSmith](https://smith.langchain.com) <br>
- [API Integration & Deployment Guide](references/deployment-guide.md) <br>
- [LangGraph Agent Patterns for Warden](references/langgraph-patterns.md) <br>
- [Warden Agent Builder - Quick Reference](references/quick-reference.md) <br>
- [Installation Guide for OpenClaw](references/installation-guide.md) <br>
- [Example Warden Agent Configurations](assets/example-configs.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, configuration examples, and scaffolded project files from bundled scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create TypeScript or Python LangGraph project files and may test HTTP health, invoke, and stream endpoints when the user runs the bundled scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
