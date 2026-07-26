## Description: <br>
Host HTML/Markdown pages and share PDF, Word, or PowerPoint docs as ShareOne short links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beep879](https://clawhub.ai/user/beep879) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agents and developers use this skill to publish HTML, Markdown, text, PDF, Word, and PowerPoint content to ShareOne, then manage passwords, watermarks, comments, downloads, refreshes, settings, and deletion for those shares. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish selected local files or conversation-derived text to a publicly reachable ShareOne link. <br>
Mitigation: Confirm the exact content and intended visibility before publishing, and use passwords or other restrictions for sensitive shares. <br>
Risk: The skill handles ShareOne API keys, which may be exposed if pasted into normal chat or captured in logs. <br>
Mitigation: Avoid sharing API keys in ordinary chat, rotate any key that appears in transcripts or logs, and use the documented credential flow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/beep879/skills/shareone) <br>
- [Publishing text and HTML pages workflow](artifact/workflows/publish-text-page.md) <br>
- [Publishing binary documents workflow](artifact/workflows/publish-binary-file.md) <br>
- [Environment and credentials workflow](artifact/workflows/environment-and-credentials.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and terminal command guidance with ShareOne URLs and status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or update public ShareOne links and may instruct the agent to handle API-key based credentials.] <br>

## Skill Version(s): <br>
1.2.7 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
