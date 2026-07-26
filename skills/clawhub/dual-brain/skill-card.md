## Description: <br>
Dual-Brain generates short alternative perspectives from a configured secondary LLM so an agent can consider another viewpoint before responding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dannydvm](https://clawhub.ai/user/dannydvm) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to run a background perspective daemon for OpenClaw sessions. It watches user messages, asks a configured secondary model for a concise second opinion, and writes that perspective for the primary agent to synthesize. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The daemon monitors OpenClaw session content and may send user messages or context to the configured LLM provider. <br>
Mitigation: Prefer a local provider for sensitive work, restrict owner or session scope, and review provider configuration before enabling continuous monitoring. <br>
Risk: API keys can be stored in ~/.dual-brain/config.json for remote providers. <br>
Mitigation: Protect the config file, avoid storing unnecessary keys, and rotate any key that may have been exposed. <br>
Risk: The skill can install a persistent background service using launchd or systemd commands. <br>
Mitigation: Run the daemon in the foreground first, review the installer before use, and enable a service only when persistent monitoring is intended. <br>
Risk: Generated perspectives, logs, state, and optional Engram memories can retain derived content from user sessions. <br>
Mitigation: Review retention needs and delete perspectives, logs, state files, or Engram memories when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dannydvm/skills/dual-brain) <br>
- [README](artifact/README.md) <br>
- [Quick Start](artifact/QUICKSTART.md) <br>
- [Agent integration guide](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown perspective files and concise text guidance, with shell commands for setup and operation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes latest perspective files under ~/.dual-brain/perspectives and can optionally store derived perspectives in local Engram when enabled.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
