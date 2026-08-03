## Description: <br>
Generates TikTok Shop ERP OAuth authorization links, lists authorized ERP shops, and supports optional token lookup or manual refresh for LinkFox TikTok Shop workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to authorize TikTok Shop ERP seller accounts, select authorized ERP shops, and support token diagnostics before using downstream TikTok Shop business skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive authorization data, including authorization links, shop identifiers, and diagnostic auth responses. <br>
Mitigation: Protect the LinkFox API key, avoid sharing generated response files, and treat local linkfox response files as sensitive. <br>
Risk: Credentialed calls can be sent to a configurable gateway endpoint. <br>
Mitigation: Leave LINKFOX_TOOL_GATEWAY and TIKTOK_SHOP_API_BASE_URL unset or pin them to the trusted LinkFox gateway before use. <br>
Risk: Manual token refresh and token lookup can expose auth state during troubleshooting. <br>
Mitigation: Use these flows only when needed for diagnostics or when explicitly requested, and rely on downstream proxy refresh behavior for normal business calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-auth) <br>
- [TikTok Shop ERP authorization API reference](artifact/references/api.md) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save full response JSON files locally; token values are masked in inline output.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
