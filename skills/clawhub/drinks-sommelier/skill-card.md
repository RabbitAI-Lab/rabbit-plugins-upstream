## Description: <br>
Expert sommelier for beers and wines. Load when the user asks for advice, talks about, or sends images related to beers or wines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johell1ns](https://clawhub.ai/user/johell1ns) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to choose beers or wines from a shelf, menu, personal list, or image based on their recorded taste profile. The skill researches identified products, scores fit, explains recommendations, suggests pairings, and flags options that do not match the user's preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps local beer and wine preference records, which may reveal personal taste patterns. <br>
Mitigation: Ask before saving or changing taste rules, and let users view, edit, pause, or delete the saved profile. <br>
Risk: The skill uses web search for products the user lists or shows, which may disclose product context through search queries. <br>
Mitigation: Limit searches to product facts needed for the recommendation and tell the user when web research is required. <br>
Risk: Recommendations can be incomplete when images are unreadable or product information cannot be found online. <br>
Mitigation: State uncertainty, ask for clearer input or a text list, and avoid inventing product characteristics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/johell1ns/skills/drinks-sommelier) <br>
- [GitHub source import](https://github.com/Johell1NS/drinks-sommelier/tree/main/skills/drinks-sommelier) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown recommendation with preference scores, rationale, alternatives, pairings, and products to avoid when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask clarifying questions when preferences, product data, or images are insufficient.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
