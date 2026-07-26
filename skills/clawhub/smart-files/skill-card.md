## Description: <br>
Secure file search, duplicate detection, organization analysis, and rename support for workspace files, with quiet mode for content suppression and force-gated boundary overrides. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Smart Files to inspect local workspaces, search file contents, find duplicates, summarize file metadata, preview cleanup candidates, and plan or perform guarded file renames and watch-mode organization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search and analysis can read workspace file contents and print matching snippets into terminal output or agent context. <br>
Mitigation: Use --quiet for sensitive searches, avoid scanning directories that may contain secrets, and review output handling before sharing logs or transcripts. <br>
Risk: --force can override the workspace boundary for scanning or watch mode, increasing exposure of external paths. <br>
Mitigation: Keep default workspace scoping for normal use and enable --force only after confirming the target path and intended monitoring behavior. <br>


## Reference(s): <br>
- [Smart Files ClawHub page](https://clawhub.ai/jlacroix82/skills/smart-files) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and terminal-style text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output may include file paths and content snippets unless --quiet is used; binary files are skipped, files over 10MB are skipped, and search results are capped.] <br>

## Skill Version(s): <br>
99.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
