## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use ShieldCortex to add local persistent memory, semantic recall, and knowledge graph support to AI agents while scanning memory and agent configuration paths for prompt injection, credential leaks, poisoning, and related threats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived memories and inspect agent conversations, configs, and selected environment files. <br>
Mitigation: Install only where local memory capture and security inspection are acceptable; review captured memories and disable auto-memory or proactive recall when handling sensitive work. <br>
Risk: The skill can modify OpenClaw hook files during bootstrap and update agent integration configuration during setup. <br>
Mitigation: Review setup actions before confirming them, disable self-heal when change control requires warn-only behavior, and remove integrations that are not needed. <br>
Risk: Cloud sync can transmit memory content if explicitly enabled by the user. <br>
Mitigation: Keep cloud sync disabled unless needed, provide an API key only for approved workflows, and use metadata-only or classification controls for sensitive memory. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jarvis-drakon) <br>
- [ShieldCortex homepage](https://shieldcortex.ai) <br>
- [ShieldCortex documentation](https://shieldcortex.ai/docs) <br>
- [npm package](https://www.npmjs.com/package/shieldcortex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local setup, memory operations, security scans, audit workflows, and optional cloud-sync configuration.] <br>

## Skill Version(s): <br>
4.47.29 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
