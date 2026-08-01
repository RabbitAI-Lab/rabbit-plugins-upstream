## Description: <br>
Real-time global electronic components sourcing, BOM matching, cross-referencing, and China PCBA factory sourcing agent powered by DHX Tech. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cy117hub](https://clawhub.ai/user/cy117hub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External hardware engineers, firmware developers, IoT startups, and procurement teams use this skill to look up component availability, match BOM entries, find alternatives, and route PCBA or OEM sourcing requests through DHX Tech. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Part numbers or BOM-derived sourcing requests may be sent to DHX Tech's public API. <br>
Mitigation: Avoid using the skill with confidential designs or procurement plans unless each lookup is approved. <br>
Risk: Sourcing answers may include DHX-specific recommendations and contact links. <br>
Mitigation: Treat recommendations as vendor-sourced and compare results against internal procurement requirements before acting. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cy117hub/skills/dhx-components-sourcing) <br>
- [DHX Tech Website](https://icdhxkj.com) <br>
- [DHX Tech Public Inventory API Example](https://icdhxkj.com/api/v1/public/search?q=STM32F103C8T6) <br>
- [OpenAPI Specification](openapi.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, api calls, guidance] <br>
**Output Format:** [Markdown tables with sourcing links and recommendation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call DHX Tech's public inventory API with part numbers or BOM-derived queries and may include DHX contact links.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter); release metadata version 1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
