## Description: <br>
Secure file search, dedup, organize, and rename for workspace files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Smart Files to inspect local workspaces, search file contents, find duplicates, summarize file metadata, review cleanup candidates, and monitor file changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool reads local file contents and can expose raw matched content when snippets are enabled. <br>
Mitigation: Keep snippets disabled unless needed, avoid scanning sensitive directories, and review terminal or agent logs before sharing output. <br>
Risk: The --force option can allow access outside the workspace boundary. <br>
Mitigation: Use workspace-scoped paths by default and require a deliberate path review before running with --force. <br>
Risk: Watch mode can retain file paths, hashes, timestamps, and change events in a local journal. <br>
Mitigation: Avoid watch mode on sensitive directories and clear memory/smart-files-journal.json when retained metadata is no longer needed. <br>
Risk: Security evidence reports disagreement between install metadata, documentation, and code about external access, persistence, and possible file modification behavior. <br>
Mitigation: Review the release documentation and manifest before deployment, run dry-run workflows first, and limit use to directories where file reads or modifications are acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jlacroix82/skills/smart-files) <br>
- [README](artifact/README.md) <br>
- [CHANGELOG](artifact/CHANGELOG.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text CLI output with markdown documentation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search snippets are opt-in; watch mode can persist file path, hash, timestamp, and change-event metadata in a local journal.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata, SKILL.md frontmatter, clawhub.yaml, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
