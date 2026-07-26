## Description: <br>
Conducts intelligent video search based on target and semantic descriptions; supports conventional target retrieval, natural language description retrieval, and vectorized model matching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search video content by object, natural-language description, or vector matching and return structured analysis reports, suggestions, and report links. It also supports cloud-based history report lookup through the configured API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send local videos, video URLs, and identity-linked metadata to the Life Emergence cloud service. <br>
Mitigation: Require explicit user approval before uploads or history retrieval, and document the exact destinations, retention policy, and deletion process before deployment. <br>
Risk: The skill quietly manages cloud identity, account login, report history, and local token storage. <br>
Mitigation: Review account creation and token storage behavior, limit access to trusted environments, and ensure users can understand and control identity-linked report retrieval. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-video-search-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON reports with report links and optional Markdown tables for history results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured analysis results, suggestions, status messages, and links to cloud-hosted reports.] <br>

## Skill Version(s): <br>
999.999.999 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
