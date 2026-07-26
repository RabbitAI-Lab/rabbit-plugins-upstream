## Description: <br>
Neural Integrated Memory Architecture provides persistent memory, emotional intelligence, and semantic recall for AI agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dmdorta1111](https://clawhub.ai/user/dmdorta1111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Nima Core to add persistent local memory, affect tracking, and semantic recall to OpenClaw-style AI agents. It is suited to agents that should remember prior conversations and inject relevant memory context before responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent hooks read conversation transcripts and inject remembered context into prompts. <br>
Mitigation: Enable the skill only for agents that require persistent memory, review hook configuration before deployment, and keep subagent and noise filtering controls enabled unless a broader capture scope is intended. <br>
Risk: Optional external embedding providers can send text outside the local environment. <br>
Mitigation: Prefer local embeddings by default and enable Voyage or OpenAI embeddings only after approving the provider, data handling, and API key exposure. <br>
Risk: Telegram delivery and precognitive cron jobs may expose or precompute sensitive context. <br>
Mitigation: Leave these jobs disabled unless their outputs and delivery channels are understood and approved. <br>
Risk: Legacy pickle memory files can be unsafe if loaded from untrusted sources. <br>
Mitigation: Do not load untrusted legacy pickle files; migrate only trusted local memory data to safer formats. <br>


## Reference(s): <br>
- [Nima Core on ClawHub](https://clawhub.ai/dmdorta1111/skills/nima-core) <br>
- [README](artifact/README.md) <br>
- [Installation Guide](artifact/INSTALL.md) <br>
- [Security Policy](artifact/SECURITY.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples; runtime behavior produces injected text context for the agent.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates persistent local memory state under ~/.nima/ and may use optional external embedding providers when configured.] <br>

## Skill Version(s): <br>
3.1.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
