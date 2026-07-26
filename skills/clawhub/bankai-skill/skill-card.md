## Description: <br>
BankAI generates Chinese banking document drafts across 59 document types from a short request or structured JSON input, using DeepSeek and built-in anti-fabrication guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[458468698](https://clawhub.ai/user/458468698) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bank employees, financial services teams, and developers use BankAI to turn natural language requests or structured JSON inputs into review-ready Chinese banking document drafts for regulatory replies, risk analysis, administrative notices, policies, and reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive banking inputs may be sent to DeepSeek by default. <br>
Mitigation: For customer, account, transaction, regulatory, personnel, or internal bank data, configure a private OpenAI-compatible endpoint with --base-url before use. <br>
Risk: Generated banking drafts may contain placeholders, omissions, or content that still requires factual and compliance review. <br>
Mitigation: Manually review every generated draft, verify all XX placeholders and supplied figures, and approve the text before internal or external submission. <br>
Risk: The skill requires a user-managed DeepSeek API key. <br>
Mitigation: Store the key in the configured environment variable, avoid embedding credentials in prompts or files, and use mock mode when previewing without a live model call. <br>


## Reference(s): <br>
- [BankAI homepage](https://www.deepwater84.cn/bankai/) <br>
- [ClawHub skill page](https://clawhub.ai/458468698/skills/bankai-skill) <br>
- [BankAI usage and operations](references/usage.md) <br>
- [BankAI scenario definitions](references/scenarios.mjs) <br>
- [DeepSeek platform](https://platform.deepseek.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text banking document drafts, with optional CLI file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided DeepSeek API key unless mock mode is used; --base-url can route requests to a private OpenAI-compatible endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
