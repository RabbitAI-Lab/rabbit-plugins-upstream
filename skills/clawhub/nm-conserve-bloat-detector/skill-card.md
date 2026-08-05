## Description: <br>
Detects codebase bloat via dead code, duplication, complexity, and doc bloat scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to audit repositories for dead code, duplication, stale documentation, dependency bloat, and growth patterns before cleanup, refactoring, or release work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup recommendations such as DELETE or ARCHIVE could remove useful code or documentation if followed without validation. <br>
Mitigation: Treat findings as advisory, review each recommendation manually, and verify references and tests before removing or archiving files. <br>
Risk: Dependency checks that query the npm registry can disclose package names or fail in confidential or air-gapped projects. <br>
Mitigation: Skip registry lookups unless network disclosure is acceptable, or run the check only in an approved environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-bloat-detector) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and YAML-style scan examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory bloat findings, confidence levels, and cleanup recommendations for user review.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
