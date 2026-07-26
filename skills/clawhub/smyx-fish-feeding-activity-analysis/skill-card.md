## Description: <br>
Analyzes post-feeding aquarium or aquaculture video through a cloud API to estimate fish gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score with alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium owners, aquaculture operators, and developers use this skill to submit post-feeding fish videos or video URLs for visual feeding-activity reports, abnormal appetite alerts, and historical report queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium or aquaculture media, video URLs, platform identity values, and generated account identifiers may be sent to publisher cloud services. <br>
Mitigation: Install only after reviewing publisher trust and user/operator consent; use non-sensitive test media when evaluating. <br>
Risk: The skill can create or reuse local user identities and store tokens for future history queries. <br>
Mitigation: Evaluate in an isolated workspace or account and review local identity/token records before reuse or removal. <br>
Risk: Feeding activity results may be mistaken for disease diagnosis or authorization to control aquarium equipment. <br>
Mitigation: Treat results as visual activity guidance, require human review for fish-health decisions, and do not allow feeding, medication, or water-change actions without explicit authorization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis fields and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save results to a local output file and can return historical report lists from the publisher cloud API.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
