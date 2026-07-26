## Description: <br>
Helps agents produce neutral, sourced comparisons of dog and cat food products from product names, links, packaging photos, or screenshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenchen91](https://clawhub.ai/user/chenchen91) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners and agent users use this skill to gather public product information, cross-check sources, and generate structured comparison tables for dog and cat food. The skill is designed for factual information organization and does not make purchasing or veterinary recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may gather product details, prices, public reviews, and images from changing public sources, so results can become stale or conflict across sources. <br>
Mitigation: Require source links, list conflicting values side by side, mark missing fields clearly, and include the query date or source context where relevant. <br>
Risk: Pet food comparisons can be mistaken for purchasing or veterinary advice. <br>
Mitigation: Keep the output neutral, avoid recommendation language, and include a disclaimer that final choices should consider the pet's health and veterinary guidance. <br>
Risk: Packaging photos or screenshots can be misread by visual analysis. <br>
Mitigation: Repeat recognized product details back to the user for confirmation and cross-check key fields against public sources before finalizing the table. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenchen91/skills/pet-food-compare-2) <br>
- [Server-resolved GitHub provenance](https://github.com/chenchen91/pet-food-compare/tree/main/skills/pet-food-compare) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown tables with sourced links and concise explanatory text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to be in Simplified Chinese and include neutral disclaimers, source links, and notes for missing or conflicting data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
