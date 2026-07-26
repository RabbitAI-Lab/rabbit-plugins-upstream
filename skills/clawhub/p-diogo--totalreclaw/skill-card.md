## Description: <br>
End-to-end encrypted, decentralized memory for OpenClaw with native memory_search and memory_get recall plus background fact capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[p-diogo](https://clawhub.ai/user/p-diogo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users install this skill to give agents persistent encrypted memory, automatic background fact capture, explicit memory writes, recall, import, export, curation, and account pairing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The plugin can read local OpenClaw conversation history and extract facts in the background. <br>
Mitigation: Install it only when cross-session automatic memory is desired, and disable or configure extraction when background capture is not acceptable. <br>
Risk: The plugin may use configured LLM provider keys while extracting or processing memories. <br>
Mitigation: Review provider configuration before installation and limit credentials to the intended account or environment. <br>
Risk: Recovery phrases and credential files are sensitive key material. <br>
Mitigation: Use the browser-based pairing flow and do not paste recovery phrases into chat or inspect credential files through an agent. <br>
Risk: The plugin contacts TotalReclaw, GitHub, and configured provider endpoints and persists encrypted memories. <br>
Mitigation: Confirm endpoint and data-retention expectations before deployment, especially in managed or shared OpenClaw environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/p-diogo/skills/totalreclaw) <br>
- [TotalReclaw Homepage](https://totalreclaw.xyz) <br>
- [TotalReclaw OpenClaw Setup Guide](https://github.com/p-diogo/totalreclaw/blob/main/docs/guides/openclaw-setup.md) <br>
- [TotalReclaw 3.3.13 Release](https://github.com/p-diogo/totalreclaw/releases/tag/v3.3.13) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, setup URLs, PINs, and memory recall text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can guide pairing, installation, explicit memory writes, memory recall, import/export, status checks, and configuration.] <br>

## Skill Version(s): <br>
3.3.13 (source: server release evidence, SKILL.md frontmatter, package.json, skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
