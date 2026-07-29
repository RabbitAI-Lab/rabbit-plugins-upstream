## Description: <br>
Analyzes child-monitoring video or media URLs with optional audio to classify facial, cry-sound, and body-motion emotion signals and return structured emotion results with soothing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, educators, and developers use this skill to submit child-monitoring media for cloud-based emotion analysis and receive structured classifications, negative-emotion alerts, soothing hints, and report links. The output is an auxiliary care reference and does not replace clinical or psychological advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes sensitive children's video or audio through configured cloud services. <br>
Mitigation: Use only with appropriate guardian or institutional consent, and confirm privacy, retention, and deletion expectations before submitting minors' media. <br>
Risk: Reports may be associated with an automatically managed identity, and user records or tokens may be stored in the workspace data directory. <br>
Mitigation: Restrict workspace access, review local data retention, and clear stored identities or tokens when they are no longer needed. <br>
Risk: The security scan verdict is suspicious because the skill combines minors' media processing, cloud submission, and silent identity handling. <br>
Mitigation: Review the skill and its configured services before installation, then test with non-sensitive sample media before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Child emotion recognition API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown text with structured JSON content and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media files or media URLs; default detail level is JSON.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release metadata; artifact frontmatter lists 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
