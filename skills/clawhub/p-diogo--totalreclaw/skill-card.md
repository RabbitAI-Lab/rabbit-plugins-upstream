## Description: <br>
End-to-end encrypted, decentralized memory for OpenClaw. A native kind:memory provider - recall is automatic via memory_search/memory_get, and facts are captured in the background. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[p-diogo](https://clawhub.ai/user/p-diogo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and agent operators use TotalReclaw to add persistent encrypted long-term memory, automatic recall, background fact capture, explicit memory saving, curation, import, and export to an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive local OpenClaw and LLM credential context and writes local state files. <br>
Mitigation: Review local state paths and credential handling before installation, especially on shared agents or systems that may process sensitive memories. <br>
Risk: The skill sends requests to TotalReclaw and configured model providers. <br>
Mitigation: Confirm the configured providers, relay URL, and data-flow expectations before using it for private or regulated memory content. <br>
Risk: The skill can export decrypted memories and may autonomously restart the OpenClaw gateway. <br>
Mitigation: Restrict export access, review operational impact of gateway restarts, and test the setup in a non-sensitive environment before broader deployment. <br>
Risk: Server security evidence flags scanner-evasion comments and plaintext local logs for review. <br>
Mitigation: Inspect those behaviors directly and resolve acceptability before trusting the release in sensitive or shared-agent deployments. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/p-diogo/skills/totalreclaw) <br>
- [Publisher profile](https://clawhub.ai/user/p-diogo) <br>
- [Release 3.4.1 changelog](https://github.com/p-diogo/totalreclaw/releases/tag/v3.4.1) <br>
- [TotalReclaw homepage](https://totalreclaw.xyz) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides OpenClaw memory tool use, setup, pairing, curation, import, export, and recovery flows; it does not produce a standalone generated artifact.] <br>

## Skill Version(s): <br>
3.4.1 (source: server release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
