## Description: <br>
Temu Global (non-US/EU) cancel-order API skill that helps agents use LinkFox gateway scripts for buyer after-sales cancellations and seller appeal or out-of-stock cancellation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and ecommerce operations teams use this skill to guide an agent through Temu Global order-cancellation workflows, including buyer after-sales cancellation review, seller cancellation appeals, out-of-stock cancellation requests, and status checks through LinkFox gateway scripts. <br>

### Deployment Geography for Use: <br>
Global (Temu Global site; excludes US/EU regional skills) <br>

## Known Risks and Mitigations: <br>
Risk: The release includes broad Temu proxy and file-download utilities beyond a narrow cancel-order workflow. <br>
Mitigation: Install only in trusted workspaces and use the generic proxy or download utilities only when they are intentionally needed for the task. <br>
Risk: Temu tokens and API responses may be stored locally by the skill's scripts. <br>
Mitigation: Use narrowly scoped Temu tokens, restrict access to local token and response files, and delete or secure saved files after use. <br>
Risk: The skill can perform live order-cancellation operations through LinkFox and Temu APIs. <br>
Mitigation: Confirm the target site, store, order identifiers, and cancellation action before executing scripts against production credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-global) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization and retrieval](references/access-token.md) <br>
- [Partner Global cancel-order catalog](references/partner-global-catalog.md) <br>
- [Cancel Order API document index](references/apis/README.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=dbd3d395963a408984b8ae7dbc5f64f9) <br>
- [Temu Global OpenAPI router](https://openapi-b-global.temu.com/openapi/router) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Files] <br>
**Output Format:** [Markdown guidance with bash commands and JSON API responses saved to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts persist complete responses under a linkfox date/session data directory; small responses print full JSON to stdout, larger responses print summaries unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
