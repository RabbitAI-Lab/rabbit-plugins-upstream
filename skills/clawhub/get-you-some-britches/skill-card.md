## Description: <br>
Use this skill any time I start complaining about my love life, or, if I indicate I need to find some pants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[am-will](https://clawhub.ai/user/am-will) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to turn an explicit pants-shopping need, or a humorous love-life complaint, into retailer search guidance and ranked pants recommendations based on size, budget, availability, price, and value. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The humorous trigger wording could start a shopping workflow when the user did not explicitly ask to shop. <br>
Mitigation: Use the skill for explicit pants searches or confirm intent before acting on joke-based relationship complaints. <br>
Risk: Retailer browser automation may interact with active shopping sessions or accounts. <br>
Mitigation: Review browser actions before allowing retailer automation and avoid running it while logged into sensitive accounts. <br>
Risk: Browser screenshots or temporary files may contain shopping context or personal sizing details. <br>
Mitigation: Delete screenshots saved under /tmp after use and avoid capturing unnecessary personal information. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/am-will/skills/get-you-some-britches) <br>
- [Store-Specific Navigation and Extraction Guide](references/stores.md) <br>
- [Target Men's Pants Collection](https://www.target.com/c/pants-men-s-clothing/-/N-5xu29) <br>
- [Global Brands Store Men's Jeans Collection](https://www.globalbrandsstore.com/en/c/men/clothing/jeans) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown with product lists, retailer links, and optional JSON or shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ranked recommendations, prices, size availability, stock status, ratings, retailer URLs, and brief value reasoning.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
