## Description: <br>
投标报价策略沙盘（Bid Pricing Strategy Sandbox）读取招标/采购文件中的评标办法，解析报价评分规则，并生成可在本地浏览器运行的交互式报价得分测算配置和使用指导。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bidders, bid evaluators, procurement consultants, and trainers use this skill to turn bid or procurement price-scoring rules into a local calculator workflow for score comparison, ranking review, and pricing scenario analysis. It focuses only on price scoring and requires users to verify formulas against the original tender or procurement document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The calculator can produce misleading pricing guidance if the scoring formula or assumptions are extracted incorrectly. <br>
Mitigation: Verify the extracted scoring formula and assumptions against the original bid or procurement document before using generated configurations. <br>
Risk: The workflow covers only price scoring and does not account for technical or commercial scoring dimensions. <br>
Mitigation: Use the calculator output alongside separate review of non-price criteria before making bid decisions. <br>
Risk: Users may rely on outputs written in a language they cannot fully review. <br>
Mitigation: Ask for the parsed formula, configuration, and guidance in a language the user can fully verify. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-pricing-strategy-sandbox) <br>
- [Formula knowledge base](formula-kb.md) <br>
- [Skill README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces calculator configuration for a bundled local HTML tool; calculations run in the user's browser and should be reviewed against source documents.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
