## Description: <br>
This skill helps an agent query Juhe Data's paid cell-tower location service with MCC, MNC, TAC/LAC, and CI values, then routes the HTTP 402 payment flow through Alipay before returning location data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up a cell tower's approximate location and nearby context from supplied MCC, MNC, TAC/LAC, and CI identifiers. The workflow is intended for paid Juhe Data lookups and requires explicit Alipay payment confirmation before the final location result is returned. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cell-tower identifiers are sent to Juhe Data and can be used to infer a location. <br>
Mitigation: Use the skill only when the user intends to share those identifiers for a location lookup, and show the submitted MCC, MNC, TAC/LAC, and CI values before the request. <br>
Risk: The workflow can require payment through linked Alipay payment skills before returning a result. <br>
Mitigation: Confirm the product name, amount, order number, user order number, and original query parameters before payment, and avoid modifying the original request payload during handoff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/cell-location) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires complete cell-tower identifiers and may hand off a full HTTP 402 payment response to an Alipay payment skill before returning location data.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
