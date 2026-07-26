## Description: <br>
Vision/image understanding for agents whose model can't read images, calling the Volcengine Ark vision API and returning structured JSON without substituting local OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vst93](https://clawhub.ai/user/vst93) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when an image, screenshot, or structured visual artifact must be understood but the primary model lacks image support or produces insufficient vision output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images, screenshots, OCR text, failure reasons, and prior model output are sent to Volcengine Ark for analysis. <br>
Mitigation: Use the skill only when that data transfer is acceptable, and avoid sensitive screenshots or proprietary documents unless approved for the environment. <br>
Risk: The skill depends on ARK_API_KEY and network reachability to the Volcengine Ark endpoint. <br>
Mitigation: Run the bundled preflight check before use and stop with the reported prerequisite issue if the check fails. <br>
Risk: Local OCR is not an equivalent fallback for visual layout or UI understanding. <br>
Mitigation: Do not substitute OCR when the API cannot run; configure the missing prerequisite or escalate to a stronger vision model. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/vst93/vision-fallback-skill) <br>
- [ClawHub skill page](https://clawhub.ai/vst93/skills/vision-fallback-skill) <br>
- [API Reference - Volcengine Ark vision](artifact/references/api-reference.md) <br>
- [Configuration - ARK_API_KEY](artifact/references/configuration.md) <br>
- [Constraints & Escalation](artifact/references/constraints.md) <br>
- [Output Format](artifact/references/output-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Structured JSON returned from a vision API response, with shell commands and guidance for setup and invocation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bash, curl, jq, file, base64, network access to Volcengine Ark, and an ARK_API_KEY.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
