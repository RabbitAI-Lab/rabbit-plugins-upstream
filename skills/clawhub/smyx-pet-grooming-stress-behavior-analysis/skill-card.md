## Description: <br>
Analyzes pet grooming session video files or URLs for stress-related behaviors such as struggling, panting, tail tucking, and other grooming-session stress signals, then returns a stress-level assessment and structured report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet groomers, veterinary clinic staff, and pet care providers use this skill to review grooming-session videos and identify observable stress behaviors that may require prompt intervention. The output is for behavior observation support and is not a disease diagnosis or behavior-correction plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet grooming media or URLs are processed by lifeemergence.com services. <br>
Mitigation: Use only media and URLs whose external processing is acceptable; avoid sensitive clinic/shop videos or internal URLs unless that handling is approved. <br>
Risk: The skill may create or reuse a local identity and store returned authentication tokens in a workspace SQLite database. <br>
Mitigation: Review the identity and token-storage behavior before installation, and isolate or remove workspace state according to local credential-handling policy. <br>
Risk: Stress-level output could be mistaken for veterinary diagnosis or behavior-correction advice. <br>
Mitigation: Use the report as observational support only and route animal welfare or medical concerns to qualified personnel. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet grooming stress behavior API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown or JSON analysis report, optionally written to a local output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include stress behavior observations, stress-level grading, recommendations, historical report listings, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
