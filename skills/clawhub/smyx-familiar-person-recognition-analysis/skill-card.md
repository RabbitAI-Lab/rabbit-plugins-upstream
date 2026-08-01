## Description: <br>
Identifies enrolled acquaintances in images or videos through face comparison and returns who appears at which location for home or office identity-check scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze uploaded images or videos against an enrolled face database and produce structured recognition reports, historical report lists, and report links for home or office monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images, videos, identity-linked report requests, and locally derived user identifiers may be sent to the configured cloud service. <br>
Mitigation: Install and run only after confirming that cloud processing of this data is acceptable for the intended privacy, consent, and compliance requirements. <br>
Risk: The skill may silently create or reuse a persistent account identity and store local tokens in the workspace data database. <br>
Mitigation: Review account creation, token storage, and workspace access controls before deployment. <br>
Risk: Recognition results are advisory and may be unsuitable for legal identity verification. <br>
Mitigation: Require human review and avoid using the output as the sole basis for legal, disciplinary, or high-impact identity decisions. <br>


## Reference(s): <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON recognition report, with optional output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include structured recognition results, historical report tables, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact SKILL.md frontmatter says 1.0.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
