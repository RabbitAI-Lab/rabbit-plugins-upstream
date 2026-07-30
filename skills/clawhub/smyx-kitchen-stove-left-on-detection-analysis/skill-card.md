## Description: <br>
Analyzes fixed kitchen camera images or video to detect when a stove appears to be on while the kitchen is unattended, then returns structured alerts and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, and smart-home developers use this skill to submit fixed kitchen camera footage or video URLs for unattended stove-left-on detection and to retrieve current or historical structured reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private kitchen camera footage or video URLs may be sent to the configured lifeemergence.com cloud service. <br>
Mitigation: Use only with informed consent from monitored people, avoid sensitive deployments unless cloud processing is acceptable, and review data handling before installation. <br>
Risk: The skill may silently create or reuse a local account identity and store account tokens locally. <br>
Mitigation: Run the skill in a controlled workspace, inspect the local data directory for smyx-api-key.txt and the SQLite user database, and remove retained tokens when no longer needed. <br>
Risk: The skill is used in a safety-relevant stove monitoring scenario where missed or incorrect alerts could affect emergency response. <br>
Mitigation: Treat outputs as assistive monitoring signals, require human verification for urgent alerts, and keep independent safety controls such as manual checks or verified smart-valve procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-kitchen-stove-left-on-detection-analysis) <br>
- [Kitchen stove detection API documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Markdown text with embedded structured JSON; optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local video files or video URLs, supports historical report listing, and may include report export links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
