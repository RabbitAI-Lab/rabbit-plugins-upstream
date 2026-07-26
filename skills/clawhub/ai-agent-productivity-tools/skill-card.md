## Description: <br>
Curated toolkit for business productivity, with installation guidance for Google Workspace CLI, task management, notes, health checks, and security scanning tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[certainlogicai](https://clawhub.ai/user/certainlogicai) <br>

### License/Terms of Use: <br>
Business Source License 1.1 <br>


## Use Case: <br>
Developers, business owners, and assistants use this skill to guide an agent through installing a curated productivity stack and shaping personal-assistant prompts for email, calendar, notes, health checks, and skill review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to install other tools that affect the user's local environment. <br>
Mitigation: Confirm each installation command and install only tools needed for the intended workflow. <br>
Risk: Google Workspace, Notion, and similar setup steps may require OAuth grants or API keys. <br>
Mitigation: Grant the least permissions needed, review scopes before approval, and avoid sharing secrets in prompts or logs. <br>
Risk: The JSONL context example could capture sensitive business or personal data if reused directly. <br>
Mitigation: Add data minimization, permissions, encryption, retention, and deletion rules before storing real context. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/certainlogicai/skills/ai-agent-productivity-tools) <br>
- [PA Guide](artifact/PA_GUIDE.md) <br>
- [Architecture](artifact/docs/ARCHITECTURE.md) <br>
- [Tone Guide](artifact/docs/TONE_GUIDE.md) <br>
- [Attribution](artifact/ATTRIBUTION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown documentation with inline shell commands and prompt templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Knowledge-pack guidance only; human review is expected before installing tools, linking accounts, or using API keys.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and target metadata; artifact files list 1.0.3 and 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
