## Description: <br>
Travel Planner HY helps agents collect travel requirements, search public travel information, build multi-day itineraries, estimate budgets, and generate markdown-style plans with optional local HTML and QR-code link output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cryptocxf](https://clawhub.ai/user/cryptocxf) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning assistants use this skill to turn destination, dates, party size, budget, and preferences into structured itineraries with attraction, transport, lodging, packing, and safety guidance. It is for planning and display; bookings and payments remain outside the skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated prices, QR codes, and third-party booking or payment links may be mistaken for completed checkout or final pricing. <br>
Mitigation: Treat all prices, QR codes, and Tuniu/12306 or other third-party links as references only; confirm orders and payments directly on the official third-party site. <br>
Risk: Travel web lookups and optional comparison flows can send itinerary details such as destination, dates, party size, and budget to public travel or map services. <br>
Mitigation: Use the skill only when these lookups are acceptable, and keep comparison flows opt-in before sending travel details to third-party services. <br>
Risk: The skill writes generated itinerary HTML and QR assets locally. <br>
Mitigation: Review generated files in the local output/ directory and remove them when they are no longer needed. <br>


## Reference(s): <br>
- [Travel Planner HY on ClawHub](https://clawhub.ai/cryptocxf/skills/travel-planner-hy) <br>
- [Parameters and Natural Language Parsing Rules](references/parameters.md) <br>
- [Validation Rules and Multimodal Boundaries](references/validation.md) <br>
- [Attraction Data Model and Retrieval Rules](references/attraction-model.md) <br>
- [Search and Filtering Rules](references/search-rules.md) <br>
- [Itinerary Rules](references/itinerary-rules.md) <br>
- [Output Templates](references/output-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown travel plans, structured travel parameters, and optional local HTML/QR-code files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write generated itinerary HTML and QR assets to output/; third-party booking or payment links are references only.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
