## Description: <br>
Agent Social Reader helps an agent read and summarize user-specified public web, social media, video, and RSS links, and save the retrieved item to Notion, Obsidian, or ima only when explicitly requested. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hermiod99-vibe](https://clawhub.ai/user/hermiod99-vibe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent to retrieve and summarize a specific public URL or RSS feed, including social posts and video links. When explicitly requested, it can archive the current item to Notion, Obsidian, or ima. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional web search, third-party reader services, or cloud transcription may receive user-specified URLs or media when required for a request. <br>
Mitigation: Use free or local tools first, ask before OpenAI Whisper transcription or cloud uploads, and call only the service needed for the current request. <br>
Risk: Service credentials may be read from environment variables or, with user approval, a local plaintext config file. <br>
Mitigation: Prefer platform secret storage, existing authenticated connectors, environment variables, or a secret manager; use plaintext config only after explicit approval. <br>
Risk: Saving content to Notion, Obsidian, or ima can disclose retrieved content to the selected destination. <br>
Mitigation: Save only when the active user request explicitly names or confirms that destination for the current item. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hermiod99-vibe/skills/agent-social-reader) <br>
- [Project Homepage](https://github.com/hermiod99-vibe/Agent-Social-Reader) <br>
- [Tool Details](references/tool-details.md) <br>
- [Save Scripts](references/save-scripts.md) <br>
- [Jina Reader](https://jina.ai/reader) <br>
- [FxTwitter API](https://github.com/FixTweet/FxTwitter) <br>
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) <br>
- [AgentLens API](https://agentlensapi.io) <br>
- [OpenAI Whisper API](https://platform.openai.com/docs/guides/speech-to-text) <br>
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with inline shell commands, API call examples, and optional generated archive content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce temporary /tmp/asr_* media files during requested media workflows; cleanup is previewed before deletion and requires confirmation.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
