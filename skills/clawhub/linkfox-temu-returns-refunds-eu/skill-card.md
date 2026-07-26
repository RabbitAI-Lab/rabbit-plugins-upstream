## Description: <br>
This skill helps agents use LinkFox gateway scripts for Temu EU returns, refunds, and after-sales APIs, including after-sales lists and details, return logistics, return addresses, return labels, signatures, carriers, and signed file downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu merchants, operators, and developers use this skill to retrieve and process EU returns/refunds and after-sales data through LinkFox-mediated Temu Partner API calls. It is most useful when an agent needs structured API guidance, ready-to-run scripts, token setup guidance, and saved JSON responses for returns/refunds workflows. <br>

### Deployment Geography for Use: <br>
Europe (Temu EU marketplace contexts) <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access LinkFox and Temu merchant credentials and potentially sensitive returns, order, shipping, and customer data. <br>
Mitigation: Install only in environments approved for those credentials and data, scope tokens to the needed Temu store and purpose, and avoid sharing command lines or logs that contain unmasked credentials. <br>
Risk: The generic proxy and signed file-download scripts expose broader API and download capabilities than the dedicated returns/refunds scripts. <br>
Mitigation: Prefer the dedicated returns/refunds scripts for routine workflows and review generic proxy or file-download requests before execution. <br>
Risk: Local token storage can keep Temu access tokens in plaintext. <br>
Mitigation: Avoid local token storage when possible; otherwise protect the token store path, use a dedicated TEMU_TOKEN_STORE_PATH, and remove stale tokens regularly. <br>
Risk: Saved response files may contain sensitive return, refund, order, shipping, or customer data. <br>
Mitigation: Regularly delete locally saved response files and restrict access to the linkfox output directory. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-eu) <br>
- [API Reference](references/api.md) <br>
- [Temu accessToken Authorization](references/access-token.md) <br>
- [Partner EU Returns & Refunds Catalog](references/partner-eu-catalog.md) <br>
- [Returns & Refunds API Index](references/apis/README.md) <br>
- [Temu Partner EU Documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON request/response data; scripts save full API responses as JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full responses are saved under linkfox/<date>/<session>/data; small responses may print inline, while larger responses print summaries unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
