## Description: <br>
Secure file search, dedup, organize, and rename for workspace files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Smart Files to search file contents, find duplicates, inspect metadata, analyze cleanup candidates, preview renames, and monitor workspace changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recursive file search and analysis can read sensitive workspace content. <br>
Mitigation: Use the tool only on intended directories, avoid secret-heavy paths, and keep snippets disabled unless raw matched content is explicitly needed. <br>
Risk: Snippet mode can print unredacted file content to stdout and agent context. <br>
Mitigation: Run searches without --snippets by default and review output handling before enabling snippets. <br>
Risk: Watch mode persists file paths, hashes, sizes, timestamps, and change events in a local journal. <br>
Mitigation: Run watch mode only where metadata persistence is acceptable and clear memory/smart-files-journal.json when the audit trail is no longer needed. <br>
Risk: --force can allow scanning outside the workspace and can enable file-moving behavior in watch workflows. <br>
Mitigation: Use --force only for deliberately selected paths after a dry run, and review the affected directory before enabling modifications. <br>


## Reference(s): <br>
- [ClawHub smart-files page](https://clawhub.ai/jlacroix82/skills/smart-files) <br>
- [README](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Files] <br>
**Output Format:** [Terminal text with optional JSON configuration and local file operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search snippets are hidden by default; watch mode can persist path, hash, size, timestamp, and change-event metadata to a local journal.] <br>

## Skill Version(s): <br>
99.0.3 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
