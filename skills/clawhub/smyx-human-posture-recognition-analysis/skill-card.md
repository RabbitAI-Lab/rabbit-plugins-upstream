## Description: <br>
Recognizes standing, sitting, lying down, bending, raised hands, running, falling, and other human postures, with abnormal posture detection and fall warnings for monitoring and care scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to analyze local or URL-based monitoring media through a vendor cloud service and receive structured posture-recognition reports, fall-alert results, report links, and report-history listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Posture or monitoring videos are sent to vendor cloud services for analysis. <br>
Mitigation: Use only with media approved for vendor processing, and confirm retention and deletion expectations before using sensitive home, care, or security footage. <br>
Risk: The skill silently creates or reuses a local identity and can fetch cloud report history. <br>
Mitigation: Run it only in workspaces where local identity reuse and cloud-linked report history are acceptable, and review account-control expectations before deployment. <br>
Risk: Account tokens are stored locally in the workspace data area. <br>
Mitigation: Restrict workspace access, avoid shared workspaces for sensitive use, and clear stored identity data when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON text, with optional saved output file and report link.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local video files or video URLs; supports basic, standard, and json detail levels plus cloud report-history listing.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
