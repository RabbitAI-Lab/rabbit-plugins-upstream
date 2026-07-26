## Description: <br>
高德地图综合服务，支持POI搜索、路径规划、旅游规划、周边搜索和热力图数据可视化. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[simon2256928](https://clawhub.ai/user/simon2256928) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to search Amap/Gaode places, find nearby points of interest, plan routes, generate travel plans, and create map or heatmap links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact includes a config.json with an apparent Amap API key. <br>
Mitigation: Treat the bundled key as exposed, replace it with your own AMAP_WEBSERVICE_KEY, and avoid sharing local configuration files. <br>
Risk: The skill sends a telemetry call to Amap before map operations. <br>
Mitigation: Install only when that telemetry is acceptable for the intended environment, or review and remove the telemetry calls before deployment. <br>
Risk: The Python workflow communicates with a local Electron app over a Unix socket. <br>
Mitigation: Use that workflow only with a trusted companion app, or remove it if local app IPC is not required. <br>


## Reference(s): <br>
- [Amap Web Service API Overview](https://lbs.amap.com/api/webservice/summary) <br>
- [Create an Amap Application and Key](https://lbs.amap.com/api/webservice/create-project-and-key) <br>
- [Amap POI Search API Documentation](https://lbs.amap.com/api/webservice/guide/api-advanced/newpoisearch) <br>
- [ClawHub Skill Page](https://clawhub.ai/simon2256928/skills/amap-lbs-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with URLs, JSON API results, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require AMAP_WEBSERVICE_KEY, node, python3, and the axios package.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter, server release, artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
