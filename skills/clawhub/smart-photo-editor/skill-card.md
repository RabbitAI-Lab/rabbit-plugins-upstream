## Description: <br>
AI-powered photo editing and restoration skill for smart object removal, background removal, old photo restoration, and basic edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guoxh](https://clawhub.ai/user/guoxh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative teams use this skill to route photo-editing requests to deterministic tools or AI-backed editing for object removal, restoration, background removal, portrait retouching, crop, resize, and correction workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected photos and metadata may be processed by external AI services when AI features are used. <br>
Mitigation: Use AI features only for photos that are appropriate to send to external services, and strip EXIF metadata before sharing edited images when location, device, or timestamp privacy matters. <br>
Risk: Optional R2 upload can send large reference images to a configured upload worker. <br>
Mitigation: Enable R2 upload only with a trusted worker URL and scoped token that you control. <br>
Risk: Untrusted filenames with command-like prefixes can make shell-based editing workflows harder to review safely. <br>
Mitigation: Avoid untrusted filenames with command-like prefixes and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/guoxh/skills/smart-photo-editor) <br>
- [VolcEngine Ark documentation](https://www.volcengine.com/docs/82379/2375486) <br>
- [Cloudflare R2 documentation](https://developers.cloudflare.com/r2/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify local image files when commands are executed; AI features may call external services.] <br>

## Skill Version(s): <br>
1.5.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
