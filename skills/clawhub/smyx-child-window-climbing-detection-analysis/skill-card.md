## Description: <br>
Analyzes fixed-camera window or balcony video to detect child climbing, leaning, gripping, and other high-fall-risk behaviors and return warning-oriented results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to submit window or balcony monitoring images, video files, or URLs for child climbing risk analysis and to query cloud-hosted historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes child-monitoring videos, URLs, snapshots, and reports that may contain sensitive minor and household information. <br>
Mitigation: Use only with guardian consent, send only necessary media, and treat exported reports and links as sensitive records. <br>
Risk: Analysis and history lookup use configured lifeemergence.com cloud services, which may transmit media, report metadata, and account-linked identifiers outside the local workspace. <br>
Mitigation: Confirm the configured service endpoint and data handling expectations before use, and avoid submitting regulated or unauthorized footage. <br>
Risk: The skill can create or reuse a local identity and persist tokens in the workspace data directory. <br>
Mitigation: Limit workspace access, rotate or remove stored credentials when sharing the environment, and use explicit commands for cloud history lookup. <br>
Risk: The security verdict is suspicious despite no specific scanner risk findings. <br>
Mitigation: Review the security summary and guidance before installation and run the skill only in an environment approved for sensitive child-safety media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and JSON-backed structured analysis reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include warning level, detected risk action, confidence, event time, snapshot URL, alert text, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
