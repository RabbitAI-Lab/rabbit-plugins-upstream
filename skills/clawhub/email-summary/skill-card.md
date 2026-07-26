## Description: <br>
Fetches recent emails from Gmail and provides concise summaries for inbox review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bbdyno](https://clawhub.ai/user/bbdyno) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees and individual Gmail users use this skill to review unread messages, understand key points, and identify suggested follow-up actions without opening each email manually. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes private email bodies and metadata during summarization. <br>
Mitigation: Use the skill only with mailboxes and messages appropriate for agent processing, and limit the count or query scope before summarizing. <br>
Risk: OAuth credentials and tokens grant read-only Gmail access. <br>
Mitigation: Confirm credential and token file locations before use, store them securely, and revoke or delete the OAuth token when access is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bbdyno/skills/email-summary) <br>
- [Google Cloud Console](https://console.cloud.google.com/) <br>
- [Gmail API read-only OAuth scope](https://www.googleapis.com/auth/gmail.readonly) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summary list with sender, subject, key points, and suggested actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script returns JSON email metadata and truncated message bodies for agent summarization.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
