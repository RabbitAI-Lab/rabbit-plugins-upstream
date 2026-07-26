## Description: <br>
Guides agents building, reviewing, or debugging Tencent Map JavaScript GL applications with local API references, demos, and optional API key setup helpers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to get Tencent Map JSAPI GL guidance, code examples, configuration notes, and API-specific answers for maps, overlays, visualization layers, search, routing, geocoding, administrative districts, IP location, geometry, 3D models, and performance work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional temporary key flow asks for a phone number, sends it to Tencent Map services for SMS verification, and saves the resulting temporary key locally under ~/.tencentmap/tempkey.json. <br>
Mitigation: Use a production Tencent Map key for production work, review the Tencent Map terms and privacy notices before using the temporary key flow, and replace demo keys in copied examples. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentmap-jsapi-gl-skill) <br>
- [Publisher profile](https://clawhub.ai/user/tencent-adm) <br>
- [Tencent Map JavaScript GL guide](https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Temporary key guide](artifact/tencentmap-jsapi-gl-skill/tempkey-guide.md) <br>
- [JSAPI GL reference docs](artifact/tencentmap-jsapi-gl-skill/references/jsapigl/docs/) <br>
- [Visualization reference docs](artifact/tencentmap-jsapi-gl-skill/references/visualization/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with code blocks, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference TMAP_JSAPI_KEY and local Tencent Map temporary key configuration when the user asks for key setup help.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
