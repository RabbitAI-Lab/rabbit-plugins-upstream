## Description: <br>
Voice UI is a self-evolving voice assistant UI for talking to an AI assistant, asking it to improve itself, and watching code updates in real time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yukihamada](https://clawhub.ai/user/yukihamada) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use Voice UI to run a local browser-based voice interface for an OpenClaw agent. It supports spoken chat, speech output, and voice-requested UI or code changes that can be applied and committed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The browser-accessible local service has broad agent, file, Git, and credential-related authority without sufficient control boundaries. <br>
Mitigation: Install only in an isolated workspace with a disposable or tightly limited API key, review diffs before keeping changes, and avoid running the local server while browsing untrusted sites. <br>
Risk: Spoken prompts can cause the local agent to modify files and create Git commits. <br>
Mitigation: Prefer a revised version that keeps API keys server-side, restricts CORS or allowed origins, authenticates the local agent endpoint, and asks before file edits or Git commits. <br>


## Reference(s): <br>
- [ClawHub Voice UI listing](https://clawhub.ai/yukihamada/skills/voice-ui) <br>
- [OpenClaw framework](https://github.com/openclaw/openclaw) <br>
- [OpenAI](https://openai.com) <br>
- [Anthropic](https://anthropic.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration] <br>
**Output Format:** [Browser UI responses with speech output, JSON API responses, and code or file changes committed through Git] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Voice-driven requests can invoke local agent actions that edit files and create Git commits.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence, released 2026-02-06; package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
