## Description: <br>
吃了么外卖 Agent：自动搜索附近外卖，根据口味/性价比/好评推荐，支持下单 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiamidavid00](https://clawhub.ai/user/xiamidavid00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this agent to compare nearby food-delivery options, receive recommendations based on taste, budget, ratings, delivery time, and promotions, and get assisted through cart and checkout steps without delegated payment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may handle privacy-sensitive information such as location, cuisine preferences, budget, and order history. <br>
Mitigation: Tell the agent not to store history when local memory is not desired, and review any profile, location, cart, or order details before continuing to a delivery platform. <br>
Risk: The skill references local script execution without defining specific allowed commands. <br>
Mitigation: Review any proposed local command before execution and avoid running scripts that are not necessary for comparing delivery options or preparing recommendations. <br>
Risk: The agent assists with checkout flow and could influence purchase decisions. <br>
Mitigation: Require the user to confirm restaurant choice, cart contents, delivery address, and payment details; the agent must not complete payment on the user's behalf. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xiamidavid00/skills/chi-le-me) <br>
- [Meituan Waimai search](https://waimai.meituan.com/search) <br>
- [Ele.me search](https://www.ele.me/search/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown recommendations, comparison tables, and step-by-step ordering guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ranked restaurant options, budget and delivery comparisons, menu suggestions, cart guidance, and memory update prompts.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
