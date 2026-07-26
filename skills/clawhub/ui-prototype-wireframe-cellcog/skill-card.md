## Description: <br>
Generates CellCog-powered UI prototypes and wireframes, including interactive HTML prototypes, app mockups, landing pages, mobile screens, SaaS dashboards, design systems, and user flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nitishgargiitd](https://clawhub.ai/user/nitishgargiitd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and product teams use this skill to ask an agent to create clickable UI prototypes, wireframes, app mockups, landing pages, mobile screens, SaaS dashboards, design systems, and user flows with CellCog. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, uploaded assets, mock data, branding, and generated live prototype URLs may be shareable with CellCog or stakeholders. <br>
Mitigation: Do not include production secrets, real customer data, or confidential plans unless the service access and hosting model is acceptable for the deployment. <br>
Risk: The skill depends on CELLCOG_API_KEY for CellCog access. <br>
Mitigation: Store CELLCOG_API_KEY as an environment secret and avoid embedding it in prompts, prototypes, repositories, or shared artifacts. <br>
Risk: Generated prototypes may include shareable hosted URLs and realistic sample content. <br>
Mitigation: Review generated prototypes before sharing and replace sensitive or misleading content with safe mock data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nitishgargiitd/skills/ui-prototype-wireframe-cellcog) <br>
- [Publisher profile](https://clawhub.ai/user/nitishgargiitd) <br>
- [CellCog homepage](https://cellcog.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python SDK snippets; CellCog tasks may return hosted interactive HTML prototype links, static images, or PDF artifacts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the cellcog dependency, and a CELLCOG_API_KEY environment secret.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
