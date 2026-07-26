## Description: <br>
Analyzes acoustic features of livestock and poultry vocalizations to detect abnormal sounds such as coughing, wheezing, painful screams, and hoarse calls, then outputs respiratory health risk hints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and farm operators use this skill to screen livestock or poultry audio and video recordings for abnormal vocalization patterns, respiratory risk hints, and historical analysis reports. It supports non-contact herd health monitoring but does not provide veterinary diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recordings, media URLs, and report queries are sent to the LifeEmergence/Smyx backend. <br>
Mitigation: Use only recordings and URLs approved for that backend, and avoid sensitive farm audio, incidental human speech, or private report history unless the account linkage and retention model are acceptable. <br>
Risk: The skill can create or reuse a persistent local identity and token cache automatically. <br>
Mitigation: Run it in a controlled environment, review account linkage before installation, and clear local cached credentials when the skill should no longer access prior reports. <br>
Risk: The output provides respiratory health risk hints rather than a veterinary diagnosis. <br>
Mitigation: Treat results as screening signals and confirm health decisions with professional veterinary review and appropriate laboratory testing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocalization-health-analysis-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Smyx Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON text, with optional saved output files when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include abnormal sound categories, event timing, respiratory risk level, historical report records, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
