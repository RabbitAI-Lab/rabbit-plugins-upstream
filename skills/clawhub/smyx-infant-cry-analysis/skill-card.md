## Description: <br>
Detects baby cries via audio AI in real-time, analyzes causes, and identifies needs such as hunger, tiredness, pain, discomfort, or irritability to assist new parents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, parents, and agents use this skill to analyze infant cry audio or video from a local file or public URL. It returns structured cry-cause and need identification, report links, and cloud-backed historical report listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant audio, video, or provided URLs may be sent to the Life Emergence remote service for analysis. <br>
Mitigation: Use only recordings with appropriate consent, avoid sensitive household media, and confirm retention and handling terms before deployment. <br>
Risk: The skill can silently create or reuse an account-like identity and store tokens or profile data in the workspace. <br>
Mitigation: Run it in an isolated workspace, review local data storage, and clear tokens or profile records when they are no longer needed. <br>
Risk: Cry analysis output is parenting support and may be incorrect or incomplete for medical concerns. <br>
Mitigation: Treat results as assistive guidance only and seek medical care when crying, pain, discomfort, or distress persists. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-cry-analysis) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown text with structured JSON content, report links, and optional saved result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local media paths or public media URLs; history-list output is retrieved from the remote service.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
