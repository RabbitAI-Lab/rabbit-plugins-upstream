## Description: <br>
Supports end-to-end invoice issuance workflows, including single invoice issuance, batch invoice checks, invoice previews, authorization renewal, and result handling for financial users. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ningmengyun12366](https://clawhub.ai/user/ningmengyun12366) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance and operations users use this skill to prepare, validate, preview, issue, and track invoices across single, batch, ERP order, document-based, and QR authorization scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests high-impact financial credentials and can initiate invoice-related actions. <br>
Mitigation: Use only scoped, rotatable API keys; avoid pasting long-lived credentials into chat; confirm the API key is bound only to the required invoice capability and enterprise. <br>
Risk: The release downloads and runs remote ZIP and binary artifacts. <br>
Mitigation: Install only in a controlled environment and verify downloaded ZIP and binary artifacts out of band before execution. <br>
Risk: The runtime configuration evidence includes a non-TLS default API endpoint. <br>
Mitigation: Confirm the active service endpoint uses TLS before sending invoice data or credentials. <br>
Risk: Invoice documents, task state, and configuration may be stored locally during execution. <br>
Mitigation: Use an approved workspace, restrict local file access, and review retention and cleanup requirements for invoice data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ningmengyun12366/skills/invoice-issue) <br>
- [Publisher profile](https://clawhub.ai/user/ningmengyun12366) <br>
- [Installation and update documentation](https://download.ningmengyun.com/Skills/invoice-issue/invoice-issue-install.md) <br>
- [Ningmengyun portal](https://www.nmy.cn) <br>
- [README.md](README.md) <br>
- [invoice-issue.md](references/invoice-issue/invoice-issue.md) <br>
- [batch-invoice-info-check.md](references/invoice-issue/batch-invoice-info-check.md) <br>
- [invoice-issue-auth-extend.md](references/invoice-issue/invoice-issue-auth-extend.md) <br>
- [preflight-initialization-check.md](references/common/preflight-initialization-check.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown, Files] <br>
**Output Format:** [Markdown guidance with generated shell commands, JSON task/configuration files, invoice preview/result Markdown, and local file outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before invoice issuance and may depend on local binary execution, downloaded artifacts, API-key configuration, and local task state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
