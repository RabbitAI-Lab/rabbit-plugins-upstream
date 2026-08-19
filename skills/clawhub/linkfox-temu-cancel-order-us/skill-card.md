## Description:

Provides agent-facing guidance and scripts for Temu US buyer and seller cancel-order workflows through the LinkFox gateway, including buyer after-sales cancellation list/approval and seller appeal or out-of-stock cancellation APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu US sellers, operators, and support agents use this skill to prepare and run LinkFox-mediated Partner US cancellation requests, check cancellation outcomes, and handle required LinkFox and Temu access tokens. It supports both buyer-initiated after-sales cancellation handling and seller cancellation appeal or out-of-stock workflows.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill exposes broad LinkFox/Temu gateway, file download, onboarding, and payment-related helpers beyond a narrow cancel-order wrapper.

Mitigation: Install and enable it only when those broader LinkFox/Temu helper capabilities are intentionally needed for the operating environment.

Risk: LinkFox API keys and Temu access tokens are sensitive credentials, and the artifact supports local token persistence.

Mitigation: Prefer environment or managed secret storage, restrict access to any local token store, and avoid sharing tokens in prompts, logs, screenshots, or saved artifacts.

Risk: Cancellation and payment-related actions can affect live marketplace orders or billing state.

Mitigation: Require explicit human confirmation before submitting cancellation, out-of-stock, appeal, onboarding, or payment actions.

Risk: Saved response files may contain sensitive order, cancellation, or account data.

Mitigation: Review and redact saved response files before sharing them, and do not commit session output directories to source control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-us)
- [API reference](references/api.md)
- [Partner US cancel-order interface catalog](references/partner-us-catalog.md)
- [Cancel Order API document index](references/apis/README.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Temu authorization flow](references/authorization-flow.md)
- [Temu Partner US documentation](https://partner-us.temu.com/documentation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response payloads; scripts save full JSON response files and print JSON or summaries to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and either a Temu accessToken or storeKey; full responses may include order data and are written under a LinkFox session directory.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
