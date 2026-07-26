## Description: <br>
FastAPI personalization webhook that adds persistent caller memory and dynamic context injection to ElevenLabs Conversational AI agents on Twilio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[britrik](https://clawhub.ai/user/britrik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and voice-AI operators use this skill to run a public webhook that gives ElevenLabs and Twilio voice agents caller-specific memory, daily notes, and dynamic system prompt context. It is intended for deployments where the operator controls the OpenClaw or OpenAI-compatible LLM endpoint and the required telephony credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bridge operates a public webhook that handles caller-linked personal data for personalization. <br>
Mitigation: Use strong webhook and admin secrets, HTTPS, scoped credentials, caller notice, retention and deletion practices, and enable DATA_ENCRYPTION_KEY before production use. <br>
Risk: Memories and notes are stored as plain JSON when DATA_ENCRYPTION_KEY is not configured. <br>
Mitigation: Configure DATA_ENCRYPTION_KEY for production, protect DATA_DIR permissions, and define backup and key-management procedures. <br>
Risk: Admin endpoints and cross-origin access can expose sensitive memory operations if configured too broadly. <br>
Mitigation: Keep CORS disabled unless needed, restrict ALLOWED_ORIGINS, protect admin endpoints with ADMIN_API_KEY, and monitor rate limits. <br>
Risk: Production dependency hardening remains the operator's responsibility. <br>
Mitigation: Use pinned dependencies, monitor updates, and upgrade flagged dependencies when fixed versions are available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/britrik/skills/elevenlabs-twilio-memory-bridge) <br>
- [Project homepage](https://github.com/britrik/elevenlabs-twilio-memory-bridge) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, JSON examples, Python service files, and environment-variable configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deployment and operation guidance for a FastAPI webhook service; requires ElevenLabs, Twilio, OpenClaw-compatible endpoint, public URL, admin, webhook, and phone-hash secrets.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata; artifact frontmatter and manifest list 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
