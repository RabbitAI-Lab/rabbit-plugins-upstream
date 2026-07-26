## Description: <br>
Pet Sneeze / Cough Detection analyzes pet video, with optional audio, to identify sneeze and cough events, distinguish occasional from repeated episodes, and report timing, frequency, and observations without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, veterinary staff, and boarding-center operators use this skill to analyze pet activity video or a video URL for behavior-focused sneeze and cough event detection. The skill can also retrieve prior sneeze and cough analysis reports associated with the internal service identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet video, optional audio, and report queries may be sent to the lifeemergence.com cloud service. <br>
Mitigation: Use only footage appropriate for that cloud transfer, and avoid sensitive home, clinic, or boarding footage unless the publisher provides acceptable privacy, retention, and consent controls. <br>
Risk: The skill can silently create or reuse an internal identity and store service tokens in a local workspace database. <br>
Mitigation: Review identity and token handling before installation, restrict workspace access, and remove local state when the skill is no longer needed. <br>
Risk: The skill reports behavioral observations and may miss or misclassify respiratory events. <br>
Mitigation: Treat results as observation support rather than medical diagnosis, and escalate frequent coughing, repeated sneezing, wheezing, or breathing difficulty to a veterinarian. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface reference](references/api_doc.md) <br>
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with event observations, risk level, suggestions, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include historical report tables when the user requests prior sneeze or cough reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
