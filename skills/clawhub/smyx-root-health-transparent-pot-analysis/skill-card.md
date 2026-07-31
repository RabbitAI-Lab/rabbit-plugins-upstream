## Description: <br>
Analyzes images or videos of plant roots in transparent pots or seedling boxes to score root health, assign a vitality grade, flag visual rot indicators, and suggest care adjustments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, plant-care operators, and automation agents use this skill to submit clear root images or videos from transparent pots, smart seedling boxes, plant factories, or hydroponic systems and receive a visual health assessment with care direction. It also supports cloud report-list lookup for prior analyses associated with the resolved service identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media inputs, report queries, and generated report links are sent to LifeEmergence services. <br>
Mitigation: Use only images, videos, and URLs that are appropriate to share with that external service, and avoid submitting sensitive or private media unless the deployment has approved that data flow. <br>
Risk: The skill can silently create or reuse a service identity and store user/token data in a local workspace database. <br>
Mitigation: Run it in an isolated workspace for sensitive evaluations, review the local data directory before reuse, and clear identity/token files when rotating users or test contexts. <br>
Risk: Root-health results are visual care guidance, not a definitive agronomy or pathology diagnosis. <br>
Mitigation: Treat results as decision support, verify severe root-rot findings offline, and consult a qualified plant-care or agronomy professional for high-impact interventions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-root-health-transparent-pot-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON-like structured analysis text with report links; historical report lookup returns structured text suitable for Markdown rendering.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media file paths or media URLs; documented media limit is 10 MB, and report lookup queries the external service.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
