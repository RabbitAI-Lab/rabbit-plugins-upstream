## Description: <br>
aigate helps agents operate a self-hosted OpenAI-compatible AI gateway that aggregates model routing, tool use, browser automation, media services, storage, search, messaging, and a web UI behind one local endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use aigate to bring up a Docker Compose AI gateway and give agents a single OpenAI-compatible endpoint for model routing and optional tools. It is most appropriate for trusted local or privately exposed deployments where the operator controls enabled services and tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: One bearer token can control code execution, browser automation, messaging, storage, and other enabled services. <br>
Mitigation: Operate aigate only as a trusted local or privately protected gateway, split per-service tokens before giving access to agents, and enable only the services needed for the task. <br>
Risk: .env, mailbox, Telethon, and storage data may contain sensitive secrets. <br>
Mitigation: Protect these files and data stores as secrets and avoid committing tokens or service credentials to repositories. <br>


## Reference(s): <br>
- [aigate setup](references/setup.md) <br>
- [ClawHub aigate skill page](https://clawhub.ai/psyb0t/skills/aigate) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Docker Compose setup steps, curl examples, endpoint routing guidance, and security handling notes.] <br>

## Skill Version(s): <br>
3.17.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
