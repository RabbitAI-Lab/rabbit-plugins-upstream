## Description: <br>
Based on computer vision, analyzes pet health indicators such as feeding frequency, drinking frequency, excretion status, mental state, vomiting behavior, and limping abnormalities through camera/feeder monitoring videos, promptly detects abnormal pet health conditions, and outputs health monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and pet-care operators use this skill to analyze pet monitoring images or videos for feeding, drinking, excretion, mental state, vomiting, limping, and health anomaly reporting. It can also return prior cloud report lists when the user asks for report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet monitoring media and identity-linked metadata may be sent to cloud services. <br>
Mitigation: Use the skill only when cloud processing is acceptable for the media and user context involved. <br>
Risk: The skill may silently create or reuse an identity and store authentication tokens locally. <br>
Mitigation: Review or remove any workspace data/smyx-api-key.txt value before use and account for the local SQLite user/token database that may be created in the workspace data directory. <br>
Risk: Automatic history-report triggers may query cloud report history without enough user control or disclosure. <br>
Mitigation: Prefer explicit analysis and report-history requests before invoking the cloud-backed history query behavior. <br>
Risk: Health analysis output is advisory and may be incomplete or incorrect. <br>
Mitigation: Treat reports as pet-health reference information and seek professional veterinary care for abnormal or concerning findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [JSON or Markdown health monitoring reports, with Markdown tables for historical report lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include health indicators, warnings, care suggestions, report links, and saved result files when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
