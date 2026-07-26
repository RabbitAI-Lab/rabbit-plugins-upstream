## Description: <br>
Zettelkasten is a card-box note-taking skill for capturing ideas, generating AI-style insights, detecting connections, and prompting daily review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rainy-cogmet](https://clawhub.ai/user/rainy-cogmet) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users use this skill to capture ideas as structured Zettelkasten cards, receive tags and suggested extensions, discover related notes, and review saved knowledge over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notes are persisted locally in a JSON file. <br>
Mitigation: Use the skill only for notes you are comfortable storing locally, and manage local file permissions, backups, and deletion according to your data handling needs. <br>
Risk: The bundle includes publish.sh, which can package and upload the current directory using local ClawHub credentials if run. <br>
Mitigation: Do not run publish.sh unless you intend to publish, have reviewed the directory contents that will be archived, and understand the use of the credential stored at ~/.clawhub/credentials. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rainy-cogmet/skills/zettelkasten) <br>
- [README.en.md](artifact/README.en.md) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown cards with text prompts and summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates a local JSON note database for the active user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and clawhub.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
