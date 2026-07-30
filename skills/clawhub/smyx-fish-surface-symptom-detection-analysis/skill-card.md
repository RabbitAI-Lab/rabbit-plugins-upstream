## Description: <br>
Analyzes fish aquarium or underwater camera images and videos to detect visible white-spot signs, hyperemia, and fin-rot, then returns symptom classifications, confidence, severity, guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarists, aquarium operators, ornamental fish farms, and smart-aquarium app agents use this skill to inspect fish media, classify visible body-surface symptoms, query prior reports, and produce advisory health reports without providing medication names or dosages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fish images, videos, media URLs, identifiers, and report history may be processed by the publisher's external cloud service. <br>
Mitigation: Use only non-sensitive aquarium media, avoid unrelated URLs or private camera feeds, and confirm that the deployment environment permits this external processing. <br>
Risk: The skill can silently create or reuse an internal account identity and retain service tokens in the workspace. <br>
Mitigation: Run it in a dedicated workspace, review and rotate or delete retained credentials when no longer needed, and require host-level controls before installation. <br>
Risk: Visual symptom output may be mistaken for a veterinary diagnosis or treatment plan. <br>
Mitigation: Treat outputs as visual screening guidance only, keep the no-medication constraint, and route diagnosis or treatment decisions to a qualified aquatic veterinarian or aquarium professional. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with JSON-formatted structured analysis, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call external cloud APIs for media analysis and historical report lookup; output can include symptom lists, confidence, location, severity, alert level, recommended non-drug actions, and disclaimers.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
