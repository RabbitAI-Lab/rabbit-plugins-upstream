## Description: <br>
Analyzes reptile and arachnid pet media through a cloud API to produce structured Pet Safety Guardian health reports with observed condition, possible disease risks, care suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit reptile or arachnid pet videos, files, or URLs for cloud-assisted visual health screening. It can also retrieve cloud report-history lists and return structured health findings, recommendations, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile media, video URLs, and report-history requests are sent to the Life Emergence cloud service. <br>
Mitigation: Use the skill only with user-approved media and URLs, and confirm before uploads or report-history queries. <br>
Risk: The skill can create or reuse a cloud-linked local identity and stores authentication material locally. <br>
Mitigation: Review local identity and token retention behavior, protect local data files, and avoid placing unrelated secrets in data/smyx-api-key.txt. <br>
Risk: Generated health analysis is advisory and may be incomplete or incorrect for medical decisions. <br>
Mitigation: Present results as health reference guidance and direct users to a qualified veterinarian for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports and JSON-formatted structured analysis; optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report export links, cloud report-history tables, and health reference guidance that should not replace professional veterinary diagnosis.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
