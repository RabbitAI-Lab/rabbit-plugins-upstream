## Description: <br>
Multi-tool vision context compression for LYGO that helps agents compress large prompts, logs, and tool output for Anthropic, OpenAI, Grok/xAI, and Gemini vision workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to reduce large text context before sending it to pay-per-token multimodal APIs. It is best suited for bulky logs and prompts, not byte-exact secrets, hashes, or line-precise diffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lossy PNG compression can distort exact identifiers, hashes, or line-sensitive diffs. <br>
Mitigation: Keep exact identifiers as separate verbatim text and do not rely on the image alone for byte-perfect content. <br>
Risk: The skill can read user-selected files under LYGO_STACK_ROOT and may forward upstream API requests if the local proxy is started. <br>
Mitigation: Set LYGO_STACK_ROOT deliberately, start the proxy only when intended, use least-privilege environment API keys, and review references/SECURITY.md before use. <br>
Risk: Credential files or private material could be included if the user selects them for compression. <br>
Mitigation: Do not compress .env files, vault files, private keys, credential dumps, or other secrets. <br>


## Reference(s): <br>
- [Security Guidance](references/SECURITY.md) <br>
- [LYGO Protocol Stack](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown with bash commands and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When the referenced LYGO stack tools are run, they may produce PNG context images and JSON manifests under data/pxpipe_lygo.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
