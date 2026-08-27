## Description: <br>
Persistent memory across sessions - local-first, no account needed. Automatically recalls past decisions, code, and tasks before each prompt, and saves session checkpoints. Also provides manual tools for searching, recording, and querying memory via Bash commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwin-hao-ai](https://clawhub.ai/user/edwin-hao-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to recall relevant prior decisions, tasks, and knowledge across sessions, then record useful checkpoints and structured memory for future work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud mode can send prompt text and saved memories to awareness.market when credentials are configured. <br>
Mitigation: Use local mode when sensitive work is possible, and avoid installing the skill in workspaces where prompts may contain secrets or private conversation history. <br>
Risk: The setup flow stores long-lived credentials locally and may add Awareness environment variables to the user's shell profile. <br>
Mitigation: Review local credential storage and shell profile changes after setup, keep credentials off shared machines, and clear them when the skill is no longer needed. <br>
Risk: First-run behavior can import existing OpenClaw memory and session history without a clear opt-in. <br>
Mitigation: Review existing OpenClaw memory and session files before first use, especially in workspaces that may contain secrets or private conversations. <br>
Risk: The skill can automatically start the local Awareness daemon through the actively maintained @awareness.market/local package. <br>
Mitigation: Review or preinstall the local daemon package before use, and monitor local service startup in locked-down environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/edwin-hao-ai/skills/awareness-memory) <br>
- [Awareness SDK source link from skill text](https://github.com/everest-an/Awareness-SDK) <br>
- [Awareness local endpoint](http://localhost:37800) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text context with XML-wrapped recall snippets, plus command-line setup and memory commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; supports darwin, linux, and win32 according to ClawHub metadata.] <br>

## Skill Version(s): <br>
0.3.11 (source: server release evidence and changelog, released 2026-07-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
