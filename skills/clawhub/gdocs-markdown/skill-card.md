## Description: <br>
Creates Google Docs from Markdown files by converting Markdown to DOCX and uploading it through Google Drive with the user's authenticated gog CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[techlaai](https://clawhub.ai/user/techlaai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and document authors use this skill to create editable Google Docs from Markdown content when gog can create, export, read, and copy Docs but cannot write content directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper uploads selected Markdown content to Google Drive using the user's existing gog authentication. <br>
Mitigation: Confirm which Google account gog is authenticated to and use the skill only for files intended to be stored in Google Docs. <br>
Risk: The helper may download Pandoc at runtime if the expected binary is not already available. <br>
Mitigation: Install Pandoc from a trusted package manager or verify the downloaded Pandoc release before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/techlaai/skills/gdocs-markdown) <br>
- [Pandoc 3.1.11 release archive](https://github.com/jgm/pandoc/releases/download/3.1.11/pandoc-3.1.11-linux-amd64.tar.gz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command output links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce a Google Docs URL after uploading converted content through gog.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence, created 2026-02-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
