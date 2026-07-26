## Description: <br>
Helps agents work with LinkFox gateway scripts and references for Temu EU buyer and seller order-cancellation APIs, including after-sales cancellation handling, seller cancellation appeals, and out-of-stock cancellation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu EU sellers, operators, and developer agents use this skill to route cancellation-related tasks through LinkFox and Temu Partner EU APIs, inspect cancellation statuses, submit buyer-agree, seller-appeal, and out-of-stock cancellation requests, and save response JSON for review. <br>

### Deployment Geography for Use: <br>
Europe (Temu Partner EU workflows); use depends on the seller's Temu region, account authorization, and token permissions. <br>

## Known Risks and Mitigations: <br>
Risk: Broad proxy and file-download helpers can expand what the agent can access beyond the named cancellation flows. <br>
Mitigation: Use least-privilege Temu tokens and run the generic proxy or file-download helpers only when the task explicitly requires them. <br>
Risk: Saved API responses may contain sensitive Temu order or after-sales data. <br>
Mitigation: Keep generated ./linkfox response files in a protected workspace, avoid unnecessary inline output in logged sessions, and remove or archive response files according to the store's data-handling policy. <br>
Risk: Token listing or retrieval helpers can expose authentication context in shared or logged environments. <br>
Mitigation: Avoid token-list and token-get helpers in shared sessions, prefer direct least-privilege tokens for one-off work, and restrict access to any configured token store. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-eu) <br>
- [Partner EU Catalog](references/partner-eu-catalog.md) <br>
- [API Reference](references/api.md) <br>
- [Access Token Guide](references/access-token.md) <br>
- [Authorization Flow](references/authorization-flow.md) <br>
- [Cancel Order API Index](references/apis/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON files] <br>
**Output Format:** [Markdown guidance with shell-command examples; scripts print JSON summaries and write full JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API key plus Temu accessToken or storeKey; default scripts persist responses under ./linkfox/<date>/<session>/data.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
