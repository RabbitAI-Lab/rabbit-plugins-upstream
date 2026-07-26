## Description: <br>
Analyzes pet vocalization audio or video from a file or URL, extracts acoustic features, classifies the call into emotion categories with confidence scores, and returns audio-based emotion results without medical or behavior-modification advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to classify dog, cat, or other pet vocalizations into emotion labels and confidence distributions for companionship, boarding-center monitoring, veterinary calming assessment, or behavior-training support. The skill can also retrieve prior cloud reports associated with the local identity used by the service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet audio, video, or media URLs are sent to the Life Emergence cloud service for analysis. <br>
Mitigation: Use the skill only with media the user is permitted to share with that service, and avoid sending sensitive or private recordings unless the service terms and data handling are acceptable. <br>
Risk: The skill can create or reuse a local identity, store service tokens in a workspace SQLite database, and retrieve cloud reports tied to that identity. <br>
Mitigation: Review the local identity and token storage behavior before installation, restrict workspace access, and clear stored identity data when the skill should no longer be associated with prior cloud reports. <br>
Risk: Historical report queries may reveal previously generated cloud reports for the local identity. <br>
Mitigation: Run history queries only in contexts where showing prior reports is expected and authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocal-emotion-classification-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Pet vocal emotion API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown, JSON-like structured reports, shell command examples, and optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analysis output may include confidence scores, report links, progress or error messages, and Markdown history tables.] <br>

## Skill Version(s): <br>
1.0.3 (source: server-resolved release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
