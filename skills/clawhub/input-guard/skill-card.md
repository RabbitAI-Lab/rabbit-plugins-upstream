## Description: <br>
Input Guard scans untrusted external text for prompt injection attacks and returns severity, findings, and blocking guidance before an agent processes the content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dgriffin831](https://clawhub.ai/user/dgriffin831) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Input Guard to scan web pages, social posts, search results, API responses, or other externally sourced text before allowing an agent to reason over it; MEDIUM or higher results are intended to block processing and alert a human. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional LLM scanning modes can send scanned text to external model providers and may use locally configured API keys. <br>
Mitigation: Use the default pattern-only mode for sensitive private content, and enable --llm, --llm-only, or --llm-auto only when sending the scanned text to the selected provider is acceptable. <br>
Risk: Channel alerts and MoltThreats reporting can share source URLs and detection details outside the local workflow. <br>
Mitigation: Enable alerts and reporting only for approved destinations, and use the documented human confirmation step before submitting confirmed threats to MoltThreats. <br>


## Reference(s): <br>
- [Input Guard ClawHub Release](https://clawhub.ai/dgriffin831/skills/input-guard) <br>
- [Input Guard README](artifact/README.md) <br>
- [Input Guard Integration Guide](artifact/INTEGRATION.md) <br>
- [Input Guard Testing](artifact/TESTING.md) <br>
- [MoltThreats Taxonomy Artifact](artifact/taxonomy.json) <br>
- [prompt-guard inspiration](https://clawhub.com/seojoonkim/prompt-guard) <br>
- [promptmap prompt stealing rules](https://github.com/utkusen/promptmap/tree/main/rules/prompt_stealing) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable text, quiet severity output, or JSON with severity, score, findings, mode, and optional LLM analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Exit code 0 for SAFE or LOW and 1 for MEDIUM, HIGH, or CRITICAL; optional LLM modes may send scanned text to OpenAI, Anthropic, or configured OpenClaw gateway providers.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and CHANGELOG.md, released 2026-02-02) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
