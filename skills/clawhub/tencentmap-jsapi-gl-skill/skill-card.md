## Description:

Helps agents answer, review, debug, and write Tencent Maps JavaScript GL code using bundled API documentation, demos, and key setup guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build Tencent Maps JSAPI GL applications, including map initialization, overlays, controls, events, visualization layers, search, routing, geocoding, administrative districts, IP location, geometry calculations, 3D models, and performance tuning. Agents can use the bundled references and examples to produce code, configuration guidance, and troubleshooting advice that matches Tencent Maps APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The temporary key flow handles phone numbers, SMS verification codes, session tokens, and Tencent Maps API keys.

Mitigation: Treat those values as sensitive and run the helper scripts only when intentionally creating or reusing a Tencent Maps key.

Risk: The local temporary key configuration may store phone numbers and API keys in ~/.tencentmap/tempkey.json.

Mitigation: Review or remove ~/.tencentmap/tempkey.json after use if local persistence is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentmap-jsapi-gl-skill)
- [Tencent Maps JavaScript GL overview](https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview)
- [API reference](artifact/tencentmap-jsapi-gl-skill/references/api_reference.md)
- [JSAPI GL documentation index](artifact/tencentmap-jsapi-gl-skill/references/jsapigl/docs/概述.md)
- [Visualization reference manual](artifact/tencentmap-jsapi-gl-skill/references/visualization/docs/参考手册.md)
- [Temporary key guide](artifact/tencentmap-jsapi-gl-skill/tempkey-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference TMAP_JSAPI_KEY and Tencent Maps temporary key setup when API-key onboarding is needed.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
