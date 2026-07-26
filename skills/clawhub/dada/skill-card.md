## Description: <br>
Dada is a same-city delivery guide for platform selection, merchant API integration, order lifecycle handling, fee estimation, callbacks, and shipping constraints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to understand Dada same-city delivery scenarios, integrate merchant-side delivery APIs, handle order status callbacks, and reason about delivery fees and item restrictions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delivery integrations may involve customer, courier, address, phone, callback URL, and credential values. <br>
Mitigation: Use mock payloads during testing, redact real operational data in prompts and logs, and keep webhook logs access-controlled and minimal. <br>
Risk: API credential or signature examples could be adapted with live secrets. <br>
Mitigation: Keep app keys and app secrets out of prompts and generated examples, and review generated signing code before using it with production credentials. <br>
Risk: Guidance applied directly to production delivery workflows could affect live orders or cancellation costs. <br>
Mitigation: Validate the full order, callback, query, cancellation, and fee-estimation flow in the Dada test environment before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zhangifonly/skills/dada) <br>
- [Dada Open Platform Production API](https://newopen.imdada.cn) <br>
- [Dada Open Platform Test API](https://newopen.qa.imdada.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request examples, JSON payloads, and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; no direct tool execution.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
