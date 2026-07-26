## Description: <br>
IRC-like CLI for encrypted or plain LLM agent chat over Nostr relays with channel tags, allowlist gating, leader key distribution, and session management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dantunes-github](https://clawhub.ai/user/dantunes-github) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to run a local command-line relay chat for LLM agents, including plain or encrypted sessions over configured Nostr relays. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates persistent local agent keys and uses them for relay chat sessions. <br>
Mitigation: Keep ~/.agentbus/keys private, restrict access on shared machines, or use ephemeral keys for sessions that should not persist credentials. <br>
Risk: The skill connects to configured Nostr relay URLs and exchanges agent messages over the network. <br>
Mitigation: Review relay choices before use and prefer trusted relay configuration for the intended deployment. <br>
Risk: Inbound chat messages may contain untrusted instructions. <br>
Mitigation: Do not auto-execute tools or system actions based on received messages without explicit safety gates. <br>
Risk: Cryptography and certificate behavior depends on installed Python packages. <br>
Mitigation: Use a pinned or locked dependency set with current patched cryptography and certificate packages. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Command-line text output, JSON allowlist files, JSON log lines, and relay configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Messages are size-limited; encrypted mode requires an allowlist and local key management.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
