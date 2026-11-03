## Description:

当用户需要回答商品咨询、整理售前FAQ或起草售后解释时使用。输入商品链接或资料、买家问题与已确认的店铺规则，输出可复制回复和商家待核实事项。在线商品详情支持抖音与小红书，已有资料可直接起草；不自动发送消息或办理售后。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商商家和客服人员，用于根据商品资料与已确认的店铺规则起草售前答复、售后解释和 FAQ，并标出需要商家核实的事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online product lookups send product links or identifiers to SocialDataX and may incur API charges.

Mitigation: Share only the needed link or identifier; paste product details to draft without an online lookup.

Risk: The external CLI implementation remains unverified.

Mitigation: Review the CLI, use a fixed reviewed version, and limit its access.

Risk: An API key could be exposed if placed in chat, logs, or skill files.

Mitigation: Keep the key in supported secret storage and do not include it in prompts or generated files.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [可复制的客服回复草稿，必要时附商家待核实事项或 FAQ；不发送消息或执行售后操作。]

## Skill Version(s):

0.1.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
