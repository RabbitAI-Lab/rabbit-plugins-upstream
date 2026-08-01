## Description: <br>
Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, clinicians, and developers use this skill to analyze patient monitoring videos, images, or URLs for signs such as tremor, convulsions, stiffness, and gait abnormalities, and to retrieve cloud-stored report history. Results are assistive monitoring outputs and are not a substitute for professional medical diagnosis or clinical judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive patient videos, images, or media URLs may be sent to lifeemergence.com cloud services for analysis. <br>
Mitigation: Use only with explicit consent and approved retention, deletion, and patient-data handling terms; avoid real patient data until those controls are reviewed. <br>
Risk: The skill can silently create or reuse an internal identity and store authentication tokens in the workspace data directory. <br>
Mitigation: Run in an isolated workspace, protect or clear the workspace data directory after use, and rotate or revoke credentials when testing is complete. <br>
Risk: History queries retrieve cloud report records associated with the resolved identity. <br>
Mitigation: Confirm that the resolved identity is authorized for the requested report history and avoid exposing internal identifiers, tokens, or report links in shared outputs. <br>
Risk: The analysis is medically sensitive and may be mistaken for diagnosis. <br>
Mitigation: Present outputs as assistive monitoring information only and require professional medical review for care decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/18072937735) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Structured text or JSON analysis reports, Markdown-style history lists, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local video/image paths or public media URLs; documented supported formats are jpg, jpeg, png, mp4, avi, and mov with a 10 MB file-size limit.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
