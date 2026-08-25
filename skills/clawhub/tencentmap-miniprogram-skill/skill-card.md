## Description:

Provides Tencent Map JavaScript GL guidance, API references, and demos for building and debugging web map features, visualization layers, tools, search, routing, geocoding, and 3D model workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to ask an agent for Tencent Map JSAPI GL implementation guidance, code examples, and troubleshooting grounded in bundled docs and demos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help an agent obtain a Tencent Map temporary key using phone verification and SMS code flow.

Mitigation: Prefer configuring an existing TMAP_JSAPI_KEY; use the temporary-key flow only after the user consents to sending a phone number and SMS code to Tencent.

Risk: Temporary keys may be stored locally in plaintext configuration.

Mitigation: Review local key storage before deployment and avoid using shared or unmanaged machines for the temporary-key flow.

Risk: Server security evidence marks the release suspicious because it combines map-development guidance with credential acquisition and local key storage.

Mitigation: Review and scan the skill before installation, and restrict execution of helper scripts to trusted environments.

## Reference(s):

- [Tencent Map JavaScript GL Guide](https://lbs.qq.com/webApi/javascriptGL/glGuide/glOverview)
- [Bundled API Reference](tencentmap-jsapi-gl-skill/references/api_reference.md)
- [Temporary Key Guide](tencentmap-jsapi-gl-skill/tempkey-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/tencent-adm/skills/tencentmap-miniprogram-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference TMAP_JSAPI_KEY and, when the user consents, Tencent Map temporary-key helper scripts.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
