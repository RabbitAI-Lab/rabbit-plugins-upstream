## Description: <br>
Format, review, or rewrite Chinese official documents (gongwen) to the GB/T 9704-2012 party and government document format standard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johamwon](https://clawhub.ai/user/johamwon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, editors, and administrative document authors use this skill to convert drafts into Chinese official document layouts, review existing files for GB/T 9704-2012 compliance, and produce Word/WPS formatting instructions without changing the document's factual meaning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Formatting or rewrite guidance could introduce incorrect layout changes or unintended edits into an official document. <br>
Mitigation: Review generated text and files before official use, and preserve the original source document for comparison. <br>
Risk: Bundled helper scripts read from and write to local document paths chosen during use. <br>
Mitigation: Run scripts only on documents and output locations the user selects, and inspect generated files before sharing or filing them. <br>
Risk: Server evidence reports no server-resolved GitHub import provenance for this version. <br>
Mitigation: Use the publisher profile, release metadata, and listed file hashes as the available provenance signals when deciding whether to install. <br>


## Reference(s): <br>
- [Gongwen Formatting Guidelines](references/formatting_guidelines.md) <br>
- [ClawHub skill page](https://clawhub.ai/johamwon/skills/gongwenformat) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with normalized document text, review findings, revision instructions, formatting checklists, and optional shell commands for bundled helper scripts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Helper scripts may create user-selected .docx or .txt outputs; python-docx is needed for DOCX formatting and olefile is needed for legacy .doc extraction.] <br>

## Skill Version(s): <br>
1.1.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
