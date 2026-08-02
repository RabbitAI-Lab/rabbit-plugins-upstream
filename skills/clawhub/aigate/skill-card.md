## Description: <br>
aigate is a self-hosted AI gateway that exposes inference, MCP tools, browser automation, media generation, code execution, storage, search, messaging, forecasting, an async queue, and LibreChat behind one OpenAI-compatible endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure, run, and call a trusted self-hosted OpenAI-compatible gateway that aggregates model routing, tools, browser automation, media services, code execution, storage, messaging, and a chat UI behind one endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A single gateway token can grant access to code execution, browser automation, messaging, storage, and external provider credentials. <br>
Mitigation: Use strong unique tokens, split per-service tokens before granting agent access, and provide credentials only to agents that are trusted for the requested action. <br>
Risk: Exposing the gateway directly to untrusted networks can create a high-blast-radius service endpoint. <br>
Mitigation: Keep the gateway off the public internet, use a trusted tunnel or authenticating reverse proxy when remote access is needed, and enable only required services. <br>
Risk: Configuration files can contain plaintext service credentials and messaging account secrets. <br>
Mitigation: Protect .env, mailbox, and Telethon configuration files as secrets and avoid committing tokens or credentials to repositories. <br>


## Reference(s): <br>
- [aigate setup](artifact/references/setup.md) <br>
- [aigate ClawHub page](https://clawhub.ai/psyb0t/skills/aigate) <br>
- [aigate project homepage](https://github.com/psyb0t/aigate) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl examples, Docker Compose commands, environment variable guidance, endpoint paths, and security handling notes.] <br>

## Skill Version(s): <br>
3.17.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
