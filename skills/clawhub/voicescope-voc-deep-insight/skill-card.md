## Description: <br>
VoiceScope VOC Deep Insight helps agents analyze customer feedback by logging into VoiceScope, uploading CSV, Excel, or TXT data, and running viewpoint clustering, taxonomy generation or validation, batch tagging, and per-row sentiment, keyword, summary, scenario, or action analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[z18211674869-maker](https://clawhub.ai/user/z18211674869-maker) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer experience, product, support, and research teams use this skill to turn feedback, reviews, complaints, survey responses, and interviews into tagged datasets, viewpoint clusters, sentiment summaries, keyword lists, scenario labels, action suggestions, and exportable insight reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer feedback files may contain personal, confidential, or sensitive business information and are uploaded to the VoiceScope cloud service for analysis. <br>
Mitigation: Preview files first, confirm the exact text column, and remove unnecessary PII or confidential columns before upload. <br>
Risk: Selecting the wrong source column can analyze unintended data and consume usage quota. <br>
Mitigation: Use the preview workflow and wait for explicit user confirmation of the analysis column before starting upload or remote analysis. <br>
Risk: Browser login stores a local VoiceScope auth token on the user's machine. <br>
Mitigation: Protect the local auth file on shared machines and use the logout workflow when access should be revoked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/z18211674869-maker/skills/voicescope-voc-deep-insight) <br>
- [VoiceScope platform](https://voiceaiscope.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON status output, direct result links, and exported CSV, XLSX, or JSON result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VoiceScope authentication and explicit user confirmation of the analysis column before upload.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
