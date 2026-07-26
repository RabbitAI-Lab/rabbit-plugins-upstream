## Description: <br>
Helps agents gather, cross-check, and present neutral comparisons of online dog-food and cat-food products, including ingredients, nutrition, price, origin, manufacturer, packaging images, product events, and review-language summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenchen91](https://clawhub.ai/user/chenchen91) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners and shopping assistants use this skill to organize factual dog-food and cat-food product information into neutral Markdown comparison tables. The skill is designed for information collection and comparison, not purchase decisions or veterinary advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet-food comparisons can be mistaken for health, dietary, or purchase advice. <br>
Mitigation: Keep outputs neutral and informational, include the skill's disclaimer, and direct users to verify labels, official product pages, and a veterinarian for allergies, obesity, urinary issues, prescription diets, or medical conditions. <br>
Risk: Product labels, pricing, ingredients, formulas, recalls, and reviews can change over time. <br>
Mitigation: Include source links and query dates where available, surface conflicting values instead of choosing one, and ask users to confirm current information from official sources. <br>
Risk: User-provided packaging photos or screenshots may be misread by vision/OCR tools. <br>
Mitigation: Restate recognized product and label details for user confirmation before building the comparison, and cross-check key nutrition and ingredient fields against independent sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenchen91/skills/pet-food-compare) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Guidance] <br>
**Output Format:** [Markdown tables with source links, summaries, and neutral disclaimers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to include concise Simplified Chinese prose, product comparison tables, source URLs, data-conflict notes, and a disclaimer that the comparison is informational only.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
