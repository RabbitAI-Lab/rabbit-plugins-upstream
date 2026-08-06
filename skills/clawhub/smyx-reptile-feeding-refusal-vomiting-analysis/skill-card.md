## Description: <br>
Analyzes fixed reptile enclosure feeding and post-feeding videos to detect prey attack, swallowing, feeding refusal, and regurgitation, then reports abnormal feeding events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, vivarium operators, reptile farms, and developers use this skill to analyze enclosure video for feeding behavior, refusal, vomiting, alert level, recommended non-medication actions, and report links. It is intended to support monitoring workflows and should not be treated as a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile enclosure footage, supplied video URLs, account identifiers, and report history may be sent to the vendor cloud. <br>
Mitigation: Install only for accounts and workspaces where that data sharing is acceptable, and confirm consent, retention, and deletion controls with the publisher before use. <br>
Risk: The skill creates or reuses account identity and stores tokens locally. <br>
Mitigation: Use a dedicated workspace or account, limit access to the runtime environment, and rotate or revoke credentials when removing the skill. <br>
Risk: Analysis results can affect animal-care decisions but are not a veterinary diagnosis. <br>
Mitigation: Treat outputs as visual behavior records and monitoring guidance; use professional reptile veterinary review for persistent refusal, vomiting, or health concerns. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis) <br>
- [Reptile feeding refusal/vomiting API documentation](artifact/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include attack, swallowing, vomiting, refusal, context, alert-level, recommended-action, disclaimer, and historical-report fields.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
