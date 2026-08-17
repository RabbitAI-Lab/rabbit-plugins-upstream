## Description:

Temu 全球站电商促销 API skill that routes Partner Global Promotion activity query, candidate goods, enrollment, operation status, and goods update calls through the LinkFox gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers, marketplace operators, and agent users use this skill to work with Partner Global promotion activities: querying available campaigns, finding candidate goods, enrolling goods, checking operation results, and updating enrolled promotion goods. It is intended for LinkFox-authenticated workflows that also require Temu seller access tokens or stored token keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use LinkFox and Temu API credentials to call promotion APIs, including mutating enrollment, update, and deactivation operations.

Mitigation: Use least-privilege Temu access tokens, confirm the target store and promotion payload before execution, and require review before mutating calls are run.

Risk: Temu access tokens may be stored locally and full API responses are saved on disk.

Mitigation: Keep token storage paths and generated response directories protected, avoid pasting secrets into chat or shell history, and remove saved response files when they are no longer needed.

Risk: Generic proxy and signed file-download scripts provide broader authority than the six dedicated promotion scripts.

Mitigation: Prefer dedicated promotion scripts for normal work and use generic proxy or file-download scripts only when their broader access is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-global)
- [API reference](references/api.md)
- [Partner Global Promotion catalog](references/partner-global-catalog.md)
- [Access token guide](references/access-token.md)
- [Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples, shell commands, and saved JSON API response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a linkfox session data directory and print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
