## Description: <br>
Provides fallback multimodal image understanding for agents by calling a configured OpenAI-compatible vision API and returning structured JSON when the primary model cannot read or interpret an image. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vst93](https://clawhub.ai/user/vst93) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill when an agent's primary model cannot interpret an image. It analyzes screenshots, terminal output, mobile app views, and structured visual content through a configured vision API and returns a structured result. <br>

### Deployment Geography for Use: <br>
Global; the default Ark provider uses a mainland China endpoint, and users can switch to an OpenAI-compatible provider for other regions. <br>

## Known Risks and Mitigations: <br>
Risk: Images and optional OCR or prior model output are sent to the configured external vision API. <br>
Mitigation: Use only providers approved for the data, set VISION_BASE_URL to a trusted endpoint when needed, and avoid screenshots or documents containing secrets unless that disclosure is acceptable. <br>
Risk: The default Ark provider uses a mainland China endpoint, which may be unsuitable for some users or data handling requirements. <br>
Mitigation: Set VISION_PROVIDER=openai or configure VISION_BASE_URL and VISION_MODEL for an approved OpenAI-compatible provider. <br>
Risk: Untrusted OCR text, failure reasons, or prior model output can contain prompt-like content. <br>
Mitigation: The skill wraps those fields in untrusted-input boundaries and instructs the vision model to treat them as data rather than instructions. <br>


## Reference(s): <br>
- [Configuration](references/configuration.md) <br>
- [API Reference](references/api-reference.md) <br>
- [Output Format](references/output-format.md) <br>
- [Constraints and Escalation](references/constraints.md) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>
- [Volcengine Ark Documentation](https://www.volcengine.com/docs/82379) <br>
- [ClawHub Skill Page](https://clawhub.ai/vst93/skills/vision-fallback-skill) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Raw API JSON response with structured image-understanding JSON in choices[0].message.content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an image path, URL, or data URL; optional OCR text, failure reason, and prior model output may be supplied as context.] <br>

## Skill Version(s): <br>
1.4.3 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
