## Description: <br>
Analyzes pet hospital waiting-area videos or video URLs through a server-side service to identify anxiety-related behavior signals and return a standardized anxiety level from 1 to 5 without diagnosing disease or recommending treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Veterinary clinic staff and pet-care operators can use this skill to triage pets in waiting areas by reviewing structured anxiety signals and a 1-5 stress level. Results are intended to support workflow and comfort decisions, not clinical diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet hospital media may be processed by the vendor's cloud service. <br>
Mitigation: Use only media that the clinic is authorized to share, and avoid footage containing owners, staff, or sensitive clinic details unless consent and retention expectations are clear. <br>
Risk: The skill creates or reuses backend identities, stores tokens locally, and retrieves cloud history reports tied to that identity. <br>
Mitigation: Review identity and token handling before installation, and deploy only where persistent cloud report access is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports, including report links for cloud history queries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.8 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
