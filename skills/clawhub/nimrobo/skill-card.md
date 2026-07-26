## Description: <br>
Use the Nimrobo CLI for voice screening and matching network operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[virang-nimrobo](https://clawhub.ai/user/virang-nimrobo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to drive Nimrobo CLI workflows for voice interviews, candidate screening, matching-network posts, applications, organization administration, and messaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable broad account, hiring, messaging, and organization-control actions through the Nimrobo CLI. <br>
Mitigation: Require explicit user confirmation before onboarding, sending messages, accepting or rejecting applications, changing roles, removing members, deleting posts or organizations, or running batch operations. <br>
Risk: Stored API keys and saved Net context can cause commands to act on the wrong account, organization, post, channel, or user. <br>
Mitigation: Protect the API key file and verify saved context with `nimrobo net context show` before write, delete, role, messaging, or batch commands. <br>
Risk: Transcript, audio, profile, application, and messaging commands may expose sensitive personal or recruiting data. <br>
Mitigation: Confirm user intent and destination before exporting transcripts or audio, reading private records, or sending content to Nimrobo services. <br>
Risk: The authoritative security summary marks the release suspicious because safety guidance is not sufficiently scoped for the available capabilities. <br>
Mitigation: Install only when the Nimrobo service and npm package are trusted, and review high-impact commands before execution. <br>


## Reference(s): <br>
- [Nimrobo ClawHub Skill Page](https://clawhub.ai/virang-nimrobo/skills/nimrobo) <br>
- [Installation & Setup](artifact/installation.md) <br>
- [Nimrobo CLI Documentation](artifact/core.md) <br>
- [Command Reference](artifact/commands.md) <br>
- [Voice Commands Reference](artifact/voice-commands.md) <br>
- [Net Commands Reference](artifact/net-commands.md) <br>
- [Workflow Guide](artifact/workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that authenticate to Nimrobo, read local context, call Nimrobo APIs, emit JSON, download transcripts or audio links, update profiles and organizations, process applications, and send messages.] <br>

## Skill Version(s): <br>
0.17.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
