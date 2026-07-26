## Description: <br>
Generates a format-only .docx bid-document skeleton from tender formatting requirements, including numbering schemes, .docx chapter parsing, cover/footer/TOC configuration, and no substantive bid content generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to parse .docx tender requirements or enter chapter structures, choose numbering and page formats, and generate a format-only bid document skeleton for later human completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes uploaded .docx tender files and may create or modify local .docx and configuration outputs. <br>
Mitigation: Use explicit output filenames, keep source document backups, and review generated skeletons before adding bid content. <br>
Risk: The XML repair utility can overwrite an input .docx when no separate output path is supplied. <br>
Mitigation: Run the repair utility with a separate output filename or back up the document before using overwrite mode. <br>
Risk: Optional knowledge-base checks may use tender formatting details for lookup. <br>
Mitigation: Enable knowledge-base checks only when the user is comfortable with the platform using those formatting details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bidding-document-assistant) <br>
- [Formatting reference](artifact/references/formatting.md) <br>
- [Structure reference](artifact/references/structure.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, configuration, guidance, shell commands] <br>
**Output Format:** [.docx files, JSON configuration, and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates a format-only bid skeleton; users supply or review all substantive bid content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
