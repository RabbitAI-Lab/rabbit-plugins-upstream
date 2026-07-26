## Description: <br>
Baidu Map provides a zero-dependency Baidu Maps Web API CLI and BD-09 coordinate-system guidance for geocoding, POI search, routing, and coordinate conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call Baidu Maps Web API workflows for geocoding, reverse geocoding, POI lookup, lightweight routing, and coordinate conversion. It is especially useful when handling BD-09, WGS-84, and GCJ-02 coordinate-system differences in Baidu Maps integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI sends addresses, coordinates, POI keywords, route endpoints, and generic call parameters to Baidu Maps. <br>
Mitigation: Use only approved Baidu Maps API keys, avoid submitting sensitive location data unless permitted, and review generic call parameters before execution. <br>
Risk: The Baidu Maps server-side AK is a credential used by the CLI. <br>
Mitigation: Store BMAP_AK in a protected environment variable and apply provider-side restrictions such as IP allowlists, quotas, or monitoring where appropriate. <br>


## Reference(s): <br>
- [Baidu Map ClawHub release](https://clawhub.ai/zhangifonly/skills/baidu-map) <br>
- [Baidu Maps Open Platform](https://lbsyun.baidu.com) <br>
- [Baidu Maps API endpoint](https://api.map.baidu.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI requires BMAP_AK and sends requested map inputs to Baidu Maps.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
