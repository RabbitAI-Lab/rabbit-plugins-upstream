## Description: <br>
Exports Feishu/Lark documents to self-contained local Markdown folders with downloaded images and whiteboard thumbnails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theosunny](https://clawhub.ai/user/theosunny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to save Feishu/Lark documents as local Markdown plus assets for review, archival, or migration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the active Lark/Feishu CLI session to read the specified document. <br>
Mitigation: Confirm the document URL, account, and authorization before running the export. <br>
Risk: Document contents may be temporarily stored in /tmp/lark_fetch.json and exported files are written locally. <br>
Mitigation: Choose an approved output directory and remove temporary or exported files when they are no longer needed. <br>
Risk: Upgrade guidance can involve global npm and skill installation commands. <br>
Mitigation: Review the suggested install command and package before approving a global update. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/theosunny/skills/lark-to-anything) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; generated document output is Markdown plus local asset files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates <doc-title>/index.md and <doc-title>/assets/; failed asset downloads keep original links or placeholders.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
