## Description: <br>
Use swiftfindrefs (IndexStoreDB) to list every Swift source file referencing a symbol before find-reference tasks, missing-import fixes, and cross-module refactors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[michaelversus](https://clawhub.ai/user/michaelversus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents working on Swift/Xcode projects use this skill to find the complete set of source files that reference a symbol before editing imports, renaming symbols, deleting symbols, or performing cross-module refactors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a disclosed third-party CLI that reads Xcode DerivedData or IndexStore information. <br>
Mitigation: Review the upstream Homebrew/GitHub CLI source before using it in sensitive codebases, and use an explicit dataStorePath in CI or multi-clone setups. <br>
Risk: Missing, stale, or ambiguous Xcode index data can make the reference set incomplete or point at the wrong DerivedData folder. <br>
Mitigation: Build the project first, use verbose mode to confirm discovery when needed, and stop rather than guessing if IndexStore or DerivedData resolution fails. <br>
Risk: Refactor edits can affect files outside the intended Swift symbol reference set. <br>
Mitigation: Edit only files returned by swiftfindrefs, keep changes minimal, and validate with the project build or tests for rename, delete, and import changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/michaelversus/skills/swiftfindrefs) <br>
- [CLI reference](references/cli.md) <br>
- [Workflows](references/workflows.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [SwiftFindRefs installation source](https://github.com/michaelversus/SwiftFindRefs.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and file-list interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The referenced CLI outputs one deduplicated absolute file path per line; ordering is not semantically meaningful.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
