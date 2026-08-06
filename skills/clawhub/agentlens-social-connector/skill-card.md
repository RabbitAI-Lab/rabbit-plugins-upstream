## Description: <br>
AgentLens Social Connector helps an AI agent retrieve public social media links through the AgentLens API, summarize and interpret returned content or media, and save results to a user-confirmed knowledge base when the agent has the required capability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[inkad-code](https://clawhub.ai/user/inkad-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent read, summarize, analyze, or archive public social posts and media from supported platforms through AgentLens. It is useful when a user provides a public social URL and wants a concise explanation, transcript-aware summary, media interpretation, or knowledge-base-ready note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public social-media URLs and retrieved content or media are sent to AgentLens for retrieval. <br>
Mitigation: Install and use the skill only when that data flow is acceptable for the user's task. <br>
Risk: Video transcription, media processing, or knowledge-base saves may involve additional external services or local destinations. <br>
Mitigation: Confirm the chosen service or destination before use and perform those actions only within user-directed workflows. <br>
Risk: Credential persistence can expose API keys or destination tokens if stored in an untrusted location. <br>
Mitigation: Persist credentials only after explicit approval and only in a trusted secret store. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/inkad-code/skills/agentlens-social-connector) <br>
- [AgentLens Homepage](https://agentlensapi.io/?utm_source=clawhub&utm_content=social_connector_skill) <br>
- [AgentLens API Reference](references/agentlens-api.md) <br>
- [Media Workflows](references/media-workflows.md) <br>
- [Knowledge Base Workflows](references/knowledge-base-workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses and knowledge-base-ready notes, with JSON shown only when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include platform, author/source, title, publication date, summary, key points, transcript notes, media interpretation, source URL, and destination save status when available.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata; artifact frontmatter version 2026.08.02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
