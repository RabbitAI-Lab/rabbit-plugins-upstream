## Description: <br>
Ripgrep helps agents use rg for fast, recursive text search that respects gitignore rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arnarsson](https://clawhub.ai/user/arnarsson) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill for guidance on searching code and text with ripgrep, including file type filters, glob filters, context output, counts, and replacement previews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches that include hidden or ignored files can expose sensitive content. <br>
Mitigation: Preview matches and limit search scope before using options such as --hidden or --no-ignore. <br>
Risk: Bulk replacement pipelines can modify many files. <br>
Mitigation: Review rg results first and use version control or backups before running commands such as xargs sed -i. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arnarsson/skills/ripgrep) <br>
- [ripgrep documentation linked by the skill](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md) <br>
- [ripgrep project homepage linked by the skill](https://github.com/BurntSushi/ripgrep) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the rg command-line tool; Homebrew and apt installation options are listed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
