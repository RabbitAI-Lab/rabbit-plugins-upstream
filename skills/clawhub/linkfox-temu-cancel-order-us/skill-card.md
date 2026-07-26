## Description: <br>
Temu US cancel-order support for buyer after-sales cancellation handling and seller appeal or out-of-stock cancellation workflows through LinkFox forwarding to Partner US APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Temu US sellers and support operators use this skill to guide agents through listing buyer cancellation requests, agreeing to eligible cancellations, filing seller cancellation appeals, and checking appeal or out-of-stock cancellation results. <br>

### Deployment Geography for Use: <br>
United States (Temu US / Partner US workflows) <br>

## Known Risks and Mitigations: <br>
Risk: This skill can exercise real Temu seller cancellation, appeal, file-download, and broader proxy workflows using LinkFox and Temu credentials. <br>
Mitigation: Install only when the publisher and LinkFox gateway are trusted, use least-privileged Temu tokens for the order-shipping purpose, and review requested API types before execution. <br>
Risk: Tokens and saved response files can contain sensitive account, order, or seller operational data. <br>
Mitigation: Avoid placing real tokens in chat logs or command examples, restrict permissions on ~/.linkfox/temu-access-tokens.json, and treat generated LinkFox response files as sensitive data. <br>
Risk: The generic proxy and file-download scripts are broader than cancellation-only helper scripts. <br>
Mitigation: Prefer the specific cancel-order scripts for routine workflows and review parameters carefully before using temu_proxy.py or file-download helpers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-cancel-order-us) <br>
- [linkfox-temu-cancel-order-us API reference](references/api.md) <br>
- [Partner US cancel-order interface catalog](references/partner-us-catalog.md) <br>
- [Cancel Order interface documentation index](references/apis/README.md) <br>
- [Temu accessToken authorization and retrieval](references/access-token.md) <br>
- [Temu authorization flow](references/authorization-flow.md) <br>
- [Temu Partner US documentation](https://partner-us.temu.com/documentation) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls, Files] <br>
**Output Format:** [Markdown guidance with shell commands and JSON request or response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write full LinkFox responses to local JSON files and may print full or summarized JSON depending on response size and inline mode.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
