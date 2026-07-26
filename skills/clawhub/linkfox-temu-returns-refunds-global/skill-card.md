## Description: <br>
Helps agents use LinkFox gateway scripts and documentation for Temu Global returns, refunds, and after-sales APIs, including after-sales order lookup, return logistics, return addresses, return labels, signatures, and carrier queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and Temu sellers use this skill to call and document Temu Global return, refund, and after-sales workflows through LinkFox, including querying after-sales records, return shipping, labels, signatures, carriers, and related token setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Temu seller API access through LinkFox. <br>
Mitigation: Use the narrowest Temu token possible for order and after-sales workflows, avoid unrelated permissions, and rotate or revoke tokens when access is no longer needed. <br>
Risk: The included generic Temu proxy can be used beyond the documented return and refund APIs. <br>
Mitigation: Limit use of the generic proxy to the return, refund, and after-sales API types documented by this skill. <br>
Risk: The skill stores Temu access tokens and API response data locally, and saved responses may contain order, refund, customer, or account data. <br>
Mitigation: Protect or relocate the token store, restrict filesystem access, and periodically delete saved response files that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-returns-refunds-global) <br>
- [API reference](references/api.md) <br>
- [Temu accessToken authorization and retrieval](references/access-token.md) <br>
- [Partner Global Returns & Refunds catalog](references/partner-global-catalog.md) <br>
- [Returns & Refunds API document index](references/apis/README.md) <br>
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896) <br>
- [Temu Global OpenAPI router](https://openapi-b-global.temu.com/openapi/router) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, files, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, Python script invocations, and JSON API responses saved to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses may be printed to stdout; larger responses are summarized after saving the full JSON response.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
