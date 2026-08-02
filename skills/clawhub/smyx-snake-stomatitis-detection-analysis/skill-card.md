## Description: <br>
Analyzes snake mouth images or videos to identify visual signs such as mucosa color changes, pus points, ulcers, necrotic tissue, and a low, moderate, or high stomatitis risk level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, reptile keepers, breeders, veterinary teams, and developers use this skill to submit snake mouth images or videos for structured visual risk assessment and report retrieval. It is intended to support early observation and triage, not to provide a veterinary diagnosis or treatment plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded snake mouth images or videos and report history may be processed by the LifeEmergence cloud service. <br>
Mitigation: Avoid sensitive footage during evaluation, use a separate test workspace or account, and verify the publisher's data retention and account policies before production use. <br>
Risk: The skill can silently create or reuse local identity state and store tokens locally. <br>
Mitigation: Review local identity and token storage behavior before installation, and isolate testing from production accounts. <br>
Risk: The skill's visual output could be mistaken for veterinary diagnosis or treatment advice. <br>
Mitigation: Treat results as visual triage only and route suspected stomatitis, necrosis, deep ulcers, or repeated high-risk findings to a professional reptile veterinarian. <br>


## Reference(s): <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-snake-stomatitis-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON report with visual findings, risk level, recommended next steps, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a cloud analysis service, process uploaded media, and query historical reports tied to an internally managed identity.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
