## Description: <br>
Guides freight brokers through lane pricing and accept, counter, or pass decisions using market benchmarks, carrier costs, margin, win probability, and relationship value. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Freight brokers use this skill to quote spot lanes, compare carrier rates against market benchmarks and cost-to-cover, and choose whether to accept, counter, or pass. It is decision support for lanes where no locked contract rate already governs the price. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pricing guidance can be wrong when market benchmarks, carrier cost-to-cover, repositioning, or deadhead inputs are stale or missing. <br>
Mitigation: Verify current lane benchmarks and carrier costs before relying on the recommendation. <br>
Risk: A suggested quote, acceptance, counter, or pass decision may conflict with locked contract rates or company approval rules. <br>
Mitigation: Do not use the skill where a contract rate governs the lane, and require a human owner to approve real pricing decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/freight-lane-pricing-decision) <br>
- [deciqAI freight lane pricing decision page](https://www.deciqai.com/c/freight-lane-pricing-decision) <br>
- [Agent metadata](https://www.deciqai.com/s/freight-lane-pricing-decision.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown decision guidance with checklists and worked examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Decision-support guidance only; no executable code or hidden access.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
