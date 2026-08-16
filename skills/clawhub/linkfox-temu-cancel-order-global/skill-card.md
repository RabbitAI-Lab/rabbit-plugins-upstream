## Description:

Temu 全球站（非 US/EU）取消订单 API（买家+卖家合一），经 LinkFox 网关转发 6 个接口：买家售后取消(bg.aftersales.cancel.*)、卖家申诉/缺货取消(temu.order.cancel.*)等，默认 site=global、tokenPurpose=order-shipping。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers and operators use this skill to prepare and run LinkFox-mediated Temu Global buyer and seller order-cancellation API calls, including after-sales cancel approval, cancel appeal submission, out-of-stock cancellation, and related result checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Temu seller credentials and can make network calls to LinkFox and Temu gateways.

Mitigation: Use it only in trusted environments, provide least-privilege credentials, and confirm each order-cancellation action before execution.

Risk: The bundled behavior includes broad proxy, credential, onboarding, billing, file-download, and persistence capabilities beyond the narrow cancellation workflow.

Mitigation: Prefer a narrowed deployment limited to the six documented cancellation APIs and disable or remove unrelated proxy, file-download, billing, and onboarding workflows when they are not needed.

Risk: Access tokens and complete order/API responses may be stored on disk.

Mitigation: Mask credentials, avoid raw token export, use an approved token store path, redact persisted responses where possible, and apply local file-access controls and retention limits.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-global)
- [API reference](references/api.md)
- [Partner Global API catalog](references/partner-global-catalog.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Cancel Order API index](references/apis/README.md)
- [Onboarding and account guidance](references/onboarding.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, API calls]

**Output Format:** [Markdown guidance, shell commands, JSON request and response data, and saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts can print complete JSON for small responses, summarize larger responses, and persist full API responses under a local linkfox session data directory.]

## Skill Version(s):

1.0.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
