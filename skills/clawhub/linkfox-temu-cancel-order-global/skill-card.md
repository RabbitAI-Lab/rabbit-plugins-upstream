## Description:

Provides Temu Global cancel-order guidance and scripts for buyer after-sales cancellation and seller appeal or out-of-stock cancellation flows through the LinkFox gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers and developers use this skill to prepare and run global-region cancel-order API calls, including buyer after-sales cancellation, seller cancellation appeals, and out-of-stock cancellation review flows.

### Deployment Geography for Use:

Global, excluding the US and EU flows that the skill directs users to handle with separate regional skills.

## Known Risks and Mitigations:

Risk: The skill includes broader proxy, onboarding, file-download, account, payment, token, and local-retention capabilities than cancel-order workflows alone require.

Mitigation: Review the scripts before installation and run only the cancel-order entry points needed for the task; avoid generic proxy, onboarding, payment, and file-download commands unless those broader capabilities are intentional.

Risk: Temu access tokens and LinkFox gateway credentials can be supplied through environment variables, JSON parameters, or an optional local token store.

Mitigation: Avoid saving Temu access tokens unless necessary, restrict permissions on any token store, prefer short-lived task-specific credentials, and do not share command transcripts containing tokens.

Risk: Gateway base URLs can be overridden by environment variables, which could redirect API traffic if the workspace is not trusted.

Mitigation: Verify LinkFox gateway environment variables point to legitimate LinkFox domains before running API or file-download scripts.

Risk: Scripts may write complete API responses to a local linkfox data directory, which can retain order and account information after the task completes.

Mitigation: Use the skill only in a trusted workspace, review generated response files, and remove stored outputs when they are no longer needed.

## Reference(s):

- [API Reference](references/api.md)
- [Partner Global Cancel Order Catalog](references/partner-global-catalog.md)
- [Temu accessToken Authorization](references/access-token.md)
- [Authorization Flow](references/authorization-flow.md)
- [Onboarding and Account Guidance](references/onboarding.md)
- [Cancel Order API Index](references/apis/README.md)
- [Temu Partner Global Documentation](https://partner-global.temu.com/documentation)
- [Temu Global OpenAPI Router](https://openapi-b-global.temu.com/openapi/router)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files or printed to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts may write full gateway responses under a local linkfox data directory and summarize large responses unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
