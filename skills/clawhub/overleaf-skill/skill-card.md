## Description: <br>
Sync and manage Overleaf LaTeX projects from the command line, including pulling projects locally, pushing changes, compiling PDFs, and downloading compile outputs such as .bbl files for arXiv submissions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aloth](https://clawhub.ai/user/aloth) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and academic authors use this skill to manage Overleaf LaTeX projects through an agent-guided command-line workflow, including local editing, sync, compilation, output downloads, and arXiv packaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Overleaf session cookie provides account access if exposed. <br>
Mitigation: Treat the cookie like a password: avoid shared terminals or logs, keep credential files out of git and shared folders, and log out or revoke the browser session if exposed. <br>
Risk: Push or sync commands can modify Overleaf project contents. <br>
Mitigation: Review changes before push or sync and use dry-run previews where appropriate. <br>
Risk: The workflow depends on installing and trusting the olcli package and its publisher. <br>
Mitigation: Install only when the package and publisher are trusted, and prefer the documented npm or Homebrew distribution paths. <br>


## Reference(s): <br>
- [Overleaf API Reference](references/API.md) <br>
- [Overleaf](https://www.overleaf.com) <br>
- [olcli npm package](https://www.npmjs.com/package/@aloth/olcli) <br>
- [Homebrew tap](https://github.com/aloth/homebrew-tap) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, command references, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands for authentication, project sync, compilation, file download, upload, and arXiv packaging workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
