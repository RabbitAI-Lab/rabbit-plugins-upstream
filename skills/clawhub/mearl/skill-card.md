## Description: <br>
Mearl lets an agent operate browser pages, inspect authenticated network activity, manage API mocks and request rules, and collect page debugging data through the `mearl` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[f-loat](https://clawhub.ai/user/f-loat) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use Mearl to automate browser interactions, debug API traffic, inspect logs and analytics events, test mocks and request rules, and work with pages that require an existing browser login. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate authenticated browser sessions and use browser cookies or signed requests. <br>
Mitigation: Use it only with trusted tooling in test or approved environments, and avoid production or account-changing actions unless they are explicitly intended. <br>
Risk: Mock and request-rule capabilities can alter API responses, redirect requests, modify headers, or block traffic. <br>
Mitigation: Review active mocks and rules before and after use, scope changes to the intended domains, and remove temporary rules when testing is complete. <br>
Risk: Payload file references can cause local file contents to be sent through the Mearl workflow. <br>
Mitigation: Reference only files that are intended for the task, and do not use file references with secrets or unrelated private data. <br>
Risk: Cloud connector tokens can expose access to the connected browser workflow if shared. <br>
Mitigation: Keep connector tokens private, share connection commands only with intended operators, and stop the connector or cloud server when the workflow is finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/f-loat/skills/mearl) <br>
- [Publisher profile](https://clawhub.ai/user/f-loat) <br>
- [Mearl Chrome Web Store listing](https://chromewebstore.google.com/detail/mearl/aoehhjnofngknnjefamjbplchbolghkm) <br>
- [Mearl usage examples](references/examples.md) <br>
- [Mearl API parameter reference](references/api-reference.md) <br>
- [Mearl connection troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference browser tabs, authenticated sessions, local files, mocks, request rules, screenshots, and connector configuration depending on the requested workflow.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
