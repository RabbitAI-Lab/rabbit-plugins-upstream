## Description: <br>
Analyzes pet hospital waiting-area videos or video URLs through a cloud API to identify anxiety-related behavior signals and return a standardized anxiety level from 1 to 5 without diagnosing disease or prescribing treatment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External veterinary clinic staff, pet care operators, and agent users can use this skill to review waiting-area pet videos, surface visible stress indicators, and prioritize calming or intake workflow decisions. Results are for workflow support and behavioral observation, not clinical diagnosis or treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet waiting-area videos or URLs are sent to a configured cloud service for analysis. <br>
Mitigation: Use only videos approved for cloud processing, avoid unnecessary capture of people or clinic identifiers, and confirm consent for sensitive surroundings before use. <br>
Risk: The skill can create or reuse an internal identity, store local account tokens, and query cloud report history. <br>
Mitigation: Review the identity and token behavior before installation, run it in an environment with appropriate access controls, and limit use to operators who should see the associated report history. <br>
Risk: Anxiety levels are estimates based on visible behavior signals and may vary with species, breed, camera angle, occlusion, or video quality. <br>
Mitigation: Treat results as waiting-workflow support only and have clinic staff compare them with direct observation before prioritizing care or comfort actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-hospital-waiting-anxiety-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, files, shell commands, guidance] <br>
**Output Format:** [Structured text or JSON analysis report, with optional Markdown table output for report history and optional saved result file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include observed behavior signals, anxiety level, risk prompts, suggestions, report links, and cloud report history.] <br>

## Skill Version(s): <br>
1.0.9 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
