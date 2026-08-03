## Description: <br>
面向硬件、设备、备件和二手产品投诉，整理订单、型号、序列号、标签、图片视频、测试、兼容性、运输、保修和供应商证据，并判断补证、排查、责任判断或退换路径；一般产品或服务投诉使用 zayn-general-complaint。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer support, aftersales, and operations teams use this skill to organize hardware complaint evidence, check whether minimum facts are present, separate confirmed facts from assumptions, and choose whether to request more evidence, troubleshoot, assess responsibility, or route toward RMA and solution workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer complaint and order evidence may include customer identifiers, order details, serial numbers, images, videos, or other sensitive business data. <br>
Mitigation: Use appropriately redacted customer data where possible and avoid providing unnecessary personal, account, or supplier details. <br>
Risk: Incomplete or conflicting evidence can lead to misleading responsibility, refund, replacement, or RMA guidance. <br>
Mitigation: Require order and product matching, at least one verifiable evidence item, clear responsibility status, and human authorization before any final remedy or commitment. <br>
Risk: The artifact is a Chinese-language workflow, and the intended operating language is not clarified in the server security guidance. <br>
Mitigation: Installers and the publisher should clarify the supported operating language and review outputs carefully when users interact in other languages. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-complaint) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact examples](artifact/examples.md) <br>
- [Artifact tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown in Chinese with parameter status, facts, pending validation, evidence, risks, and recommended next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not run commands, install code, or take account actions; expects customer complaint and order evidence as input.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
