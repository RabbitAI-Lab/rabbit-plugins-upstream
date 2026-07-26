## Description: <br>
Build original LangGraph agents for Warden Protocol and prepare them for publishing in Warden Studio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kryptopaid](https://clawhub.ai/user/kryptopaid) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to create original, API-accessible LangGraph agents for Warden Protocol, test and deploy them through LangSmith Deployments or custom infrastructure, and prepare them for Warden Studio publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real API keys, wallet, portfolio, or personal data could be exposed through generated projects, logs, third-party APIs, or Git history. <br>
Mitigation: Use environment variables or a secrets manager, keep secrets out of Git and logs, and avoid sending sensitive user data to external APIs without clear user understanding and consent. <br>
Risk: Example database passwords or scaffolded deployment settings could be reused in production. <br>
Mitigation: Review all generated files before deployment, replace example credentials, and run scripts only in a project directory the user controls. <br>
Risk: Agents built for Warden Phase 1 could exceed documented platform limits by attempting wallet access or Warden-hosted storage. <br>
Mitigation: Design and test agents to remain API-accessible, isolated to one LangGraph instance, and without user wallet access or Warden infrastructure storage. <br>


## Reference(s): <br>
- [Warden Community Agents Repository](https://github.com/warden-protocol/community-agents) <br>
- [Warden Protocol Documentation](https://docs.wardenprotocol.org) <br>
- [LangSmith](https://smith.langchain.com) <br>
- [Deploy Agent on Warden Studio](https://www.clawhub.ai/Kryptopaid/warden-studio-deploy) <br>
- [API Integration & Deployment Guide](references/deployment-guide.md) <br>
- [Installation Guide for OpenClaw](references/installation-guide.md) <br>
- [LangGraph Agent Patterns for Warden](references/langgraph-patterns.md) <br>
- [Warden Agent Builder - Quick Reference](references/quick-reference.md) <br>
- [Example Warden Agent Configurations](assets/example-configs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks, generated project files, configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May scaffold TypeScript or Python LangGraph agent projects and testing commands; users must supply and protect their own external service API keys.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
