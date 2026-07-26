## Description: <br>
Detects cats, dogs, and birds in home monitoring images or video streams and returns structured pet detection results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to detect cats, dogs, and birds in uploaded or URL-based home monitoring media, produce structured reports, and retrieve prior detection reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home monitoring images and videos may be sent to lifeemergence.com or open.lifeemergence.com services for analysis. <br>
Mitigation: Review the provider's data-handling practices before installation and avoid submitting sensitive household footage unless that transfer is acceptable. <br>
Risk: The skill automatically associates requests with a local or upstream identity and may persist account tokens locally. <br>
Mitigation: Run the skill only in environments where that identity behavior is acceptable, protect local token storage, and rotate or remove stored credentials when access should end. <br>
Risk: Historical report queries access prior cloud reports tied to the resolved identity. <br>
Mitigation: Use history-listing features only for the intended account and confirm that cloud report access aligns with the user's consent and privacy expectations. <br>


## Reference(s): <br>
- [API interface reference](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration] <br>
**Output Format:** [Markdown or JSON pet detection reports, with optional saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; can list cloud-stored historical reports.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
