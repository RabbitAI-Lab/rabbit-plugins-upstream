## Description: <br>
Analyzes plant leaf images or videos to identify curl direction and margin scorch patterns, rank likely causes such as drought stress or disease, and return diagnostic guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural operators use this skill to analyze plant leaf photos, videos, or URLs for curling and scorch symptoms, then receive likely cause rankings and directional recommendations. It can also return prior cloud-stored diagnosis reports associated with the automatic user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, or submitted URLs may be sent to a cloud service in identity-bearing requests. <br>
Mitigation: Use only media and URLs appropriate for the provider boundary, and avoid sensitive or internal/private URLs unless that service boundary is acceptable. <br>
Risk: The skill may create or reuse an automatic identity and store service tokens locally. <br>
Mitigation: Review local data and token handling before installation, and remove the local data directory if the skill is uninstalled. <br>
Risk: Plant health diagnosis can be incomplete or incorrect when symptoms overlap across drought, disease, chemical injury, or nutrient stress. <br>
Mitigation: Treat results as decision support and consult field inspection or a plant-health professional before taking high-impact treatment actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-curling-scorch-diagnosis-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown or JSON diagnostic report with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include ranked likely causes, confidence, visual evidence hints, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
