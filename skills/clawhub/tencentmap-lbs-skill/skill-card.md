## Description: <br>
Tencent Map Location Services skill for POI search, nearby search, route planning, travel planning, trajectory visualization, and map data visualization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer Tencent Maps location-service requests such as finding places, searching nearby points of interest, planning routes or trips, and generating trajectory visualizations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send requests to Tencent Maps services and uses a phone-based temporary-key flow when no production key is configured. <br>
Mitigation: Install only if Tencent Maps requests and phone verification are acceptable for the user or organization; prefer an existing production API key through TMAP_WEBSERVICE_KEY when available. <br>
Risk: Temporary keys are stored locally in plaintext at ~/.tencentmap/tempkey.json. <br>
Mitigation: Review file permissions, avoid sharing the local config file, and delete ~/.tencentmap/tempkey.json when the temporary key is no longer needed. <br>
Risk: Map searches, route planning, and travel planning can disclose user-provided locations or travel intent to external services. <br>
Mitigation: Avoid entering sensitive locations or personal travel details unless sharing them with Tencent Maps is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentmap-lbs-skill) <br>
- [Tencent Location Service](https://lbs.qq.com/) <br>
- [Tencent Maps Web Service API Overview](https://lbs.qq.com/service/webService/webServiceGuide/webServiceOverview) <br>
- [Scene 1: Nearby Search](references/scene1-nearby-search.md) <br>
- [Scene 2: Detailed POI Search](references/scene2-poi-search.md) <br>
- [Scene 3: Route Planning](references/scene3-route-planning.md) <br>
- [Scene 4: Travel Planning](references/scene4-travel-planner.md) <br>
- [Scene 5: Trajectory Visualization](references/scene5-trail-map.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown guidance with command examples, Tencent Maps links, API responses, and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require the tmap-lbs CLI and TMAP_WEBSERVICE_KEY for most Tencent Maps WebService workflows; trajectory visualization does not require an API key.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
