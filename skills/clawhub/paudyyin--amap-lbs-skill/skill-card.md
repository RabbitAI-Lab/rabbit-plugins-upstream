## Description: <br>
Amap LBS Service helps agents search POIs, plan routes and tourism itineraries, find nearby places, and generate Amap/Gaode visualization links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to search places, plan routes or tourism itineraries, find nearby POIs, and visualize coordinate data with Amap/Gaode services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends external Amap requests, including usage-count telemetry before operations. <br>
Mitigation: Review before installing, use only for map-related tasks, and make users aware that Amap requests may be made. <br>
Risk: Heatmap links embed user-provided data URLs into an Amap page, which can expose private or signed data URLs. <br>
Mitigation: Avoid private or signed data URLs for heatmaps and use only data sources intended to be shared with Amap. <br>
Risk: The release evidence reports an apparent bundled Amap API key in configuration. <br>
Mitigation: Replace or remove the bundled key so requests use an account controlled by the installing user or organization. <br>


## Reference(s): <br>
- [Amap Open Platform](https://lbs.amap.com/) <br>
- [Create an Amap Web Service key](https://lbs.amap.com/api/webservice/create-project-and-key) <br>
- [Amap POI Search API documentation](https://lbs.amap.com/api/webservice/guide/api-advanced/newpoisearch) <br>
- [Amap Web Service API overview](https://lbs.amap.com/api/webservice/summary) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with map URLs and optional bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Amap/Gaode URLs, API-key setup guidance, and generated heatmap links.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
