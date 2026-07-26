## Description: <br>
Analyzes aquarium or underwater fish images and videos for visible white-spot, hyperemia, and fin-rot symptoms, returning visual classifications, confidence scores, alert levels, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarists, aquarium operators, and ornamental fish farms use this skill to screen fish media for visible surface symptoms and retrieve structured health reports. It supports early visual triage, not a veterinary diagnosis or medication plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fish images, videos, media URLs, and report history are sent to the Life Emergence cloud service. <br>
Mitigation: Use only with authorized aquarium media and review the provider's retention, deletion, and sharing terms before deployment. <br>
Risk: The skill automatically creates or reuses an account identity and stores identity tokens locally. <br>
Mitigation: Run the skill in an isolated workspace when identity separation matters, and review or clear the workspace data directory and local SQLite database before handoff. <br>
Risk: Visual symptom screening can be mistaken for a veterinary diagnosis or treatment plan. <br>
Mitigation: Present outputs as visual triage only, require professional aquarium veterinary review for diagnosis or treatment, and avoid medication names, dosages, or treatment schedules. <br>
Risk: Reflections, bubbles, substrate particles, or natural fish markings can produce false positives. <br>
Mitigation: Use clear close-range media, apply species baseline checks, and surface false-positive risk markers in user-facing results. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-surface-symptom-detection-analysis) <br>
- [Fish Surface Symptom API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis payloads and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include detected symptom type, confidence, location, severity, alert level, recommended actions, disclaimers, and cloud report export URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
