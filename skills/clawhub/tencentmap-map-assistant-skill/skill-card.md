## Description: <br>
Tencent Map Assistant lets agents use Tencent Map services for travel itinerary generation, POI search, route planning, geocoding, weather lookup, coordinate conversion, and map or mini-program guide outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to answer map, travel, and local-search requests with Tencent Map data, then return readable route, POI, weather, itinerary, QR-code, or map outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map queries, locations, itinerary content, and phone verification data may be sent to Tencent services during normal use. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting sensitive personal or confidential location details. <br>
Risk: Tencent Map API keys and temporary key records are stored in ~/.tencentmap/tempkey.json for reuse. <br>
Mitigation: Use a dedicated low-privilege key, avoid shared machines, review the local tempkey file after use, and remove stale credentials when they are no longer needed. <br>
Risk: Generated HTML maps may embed a map key. <br>
Mitigation: Do not publish generated HTML until embedded keys have been removed, restricted, or rotated according to the publisher's guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentmap-map-assistant-skill) <br>
- [Tencent Map API reference](artifact/references/api_reference.md) <br>
- [Agent usage notes](artifact/references/agent-notes.md) <br>
- [Temporary key guide](artifact/tempkey-guide.md) <br>
- [Error-code guide](artifact/references/error-codes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Natural-language responses, Markdown travel guides, HTML map code, QR-code image files, and configuration commands or snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include live Tencent Map service results, local Markdown files, generated HTML maps, and mini-program QR-code assets.] <br>

## Skill Version(s): <br>
1.5.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
