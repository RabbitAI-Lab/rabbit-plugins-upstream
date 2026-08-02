## Description: <br>
A Chinese-language fruit-photo assistant that evaluates supported fruits for ripeness, visible quality risks, variety confidence, and purchase recommendations from photos and user context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ezra-y](https://clawhub.ai/user/ezra-y) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill when they send photos or context about supported fruits and want practical buying guidance, risk checks, or ranking among candidates. It supports Monthong durian, selected non-Monthong durians, mango, avocado, and watermelon within documented limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fruit-photo advice can be mistaken for a guarantee of taste, ripeness, or food safety. <br>
Mitigation: Keep recommendations framed as purchase guidance with confidence levels and visible-evidence limits, and do not promise sweetness, internal condition, or safety when the evidence cannot support it. <br>
Risk: Color-based judgments can be unreliable under unknown, mixed, or biased lighting. <br>
Mitigation: Use the documented light-source protocol, disable color features when the user has not answered or no usable reference is present, and rely on non-color features where applicable. <br>
Risk: Reference images may be absent from text-only packages and fallback retrieval uses a fixed raw GitHub URL. <br>
Mitigation: Prefer bundled local reference images; if local and fallback images are unavailable, do not infer image contents from filenames and lower confidence for affected visual grading. <br>
Risk: Bundled anchor images are AI-generated illustrations rather than real photographs. <br>
Mitigation: Use anchors only for relative grading and user guidance, not as proof of variety identity, authenticity, or real-world defect prevalence. <br>


## Reference(s): <br>
- [Common Photo and Confidence Protocol](references/common.md) <br>
- [Output Guide](references/output-guide.md) <br>
- [Monthong Durian Guide](references/fruits/durian-monthong.md) <br>
- [Non-Monthong Durian Guide](references/fruits/durian-non-monthong.md) <br>
- [Mango Guide](references/fruits/mango.md) <br>
- [Avocado Guide](references/fruits/avocado.md) <br>
- [Watermelon Guide](references/fruits/watermelon.md) <br>
- [Anchor Image Notes](references/anchors/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands] <br>
**Output Format:** [Chinese-language Markdown prose with optional local image-analysis helper commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confidence levels, purchase recommendations, candidate rankings, concise follow-up questions, and references to bundled visual anchors.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
