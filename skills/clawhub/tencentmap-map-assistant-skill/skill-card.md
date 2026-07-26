## Description: <br>
Tencent Map Assistant lets agents use Tencent Maps services for travel planning, POI search, routing, geocoding, IP location, weather lookup, and web map or mini-program guide generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to answer location and trip-planning requests with Tencent Maps data, including POI search, routes, addresses, weather, travel guides, QR-code mini-program guides, and generated HTML maps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map searches, routes, travel-guide text, IP-location lookups, and temporary-key phone verification data are sent to Tencent services. <br>
Mitigation: Use the skill only when that data sharing is acceptable, and avoid submitting sensitive location or personal data unless the user has approved it. <br>
Risk: The temp-key flow stores the phone number and key in plaintext under ~/.tencentmap/tempkey.json, and formal keys may be saved in the skill .env file. <br>
Mitigation: Use restrictive file permissions, avoid shared machines for key setup, rotate or remove keys when no longer needed, and prefer environment variables for managed deployments. <br>
Risk: Generated HTML maps can include a Tencent Maps API key in the JSAPI script URL. <br>
Mitigation: Apply key restrictions in the Tencent console and do not publish generated maps with unrestricted or private keys. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tencent-adm/skills/tencentmap-map-assistant-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/tencent-adm) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Temporary Key Guide](artifact/tempkey-guide.md) <br>
- [Agent Notes](artifact/references/agent-notes.md) <br>
- [Tencent Maps JSAPI GL Guide](artifact/references/jsapi-guide/README.md) <br>
- [Tencent Location Service WebService Overview](https://lbs.qq.com/service/webService/webServiceGuide/webServiceOverview) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON-like API results, generated HTML map files, QR-code image files, and local configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Tencent services, save temporary or formal map keys locally, and generate map or travel-guide artifacts in the workspace.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
