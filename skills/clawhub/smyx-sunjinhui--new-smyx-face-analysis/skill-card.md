## Description: <br>
Uploads local MP4 videos or public video URLs to a third-party remote API and returns structured TCM facial diagnosis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit clear face videos or public video URLs for TCM-style facial analysis, historical report lookup, and structured health-reference output. Results are informational and should not replace professional medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face-health media and public video URLs are sent to the provider's remote service. <br>
Mitigation: Use only with consent for the people shown, avoid sensitive or third-party videos, and confirm remote submission before analysis. <br>
Risk: The skill can create or reuse a local identity, register or log in remotely, and store reusable auth tokens in the workspace data directory. <br>
Mitigation: Review token storage before deployment, restrict workspace access, and clear stored credentials when they are no longer needed. <br>
Risk: Health-related TCM facial diagnosis output may be misleading if treated as medical advice. <br>
Mitigation: Present results as informational only and route medical decisions to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-face-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Face analysis API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown and JSON-like structured analysis reports, with optional saved output files and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include facial analysis summaries, health-reference suggestions, historical report tables, and remote report URLs.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and target metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
