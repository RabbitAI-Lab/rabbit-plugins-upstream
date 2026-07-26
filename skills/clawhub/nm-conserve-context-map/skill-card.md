## Description: <br>
Generates a compressed project context map to avoid expensive Read/Grep calls at session start or before implementing features in an unfamiliar codebase. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect an unfamiliar codebase, identify structure, dependencies, entry points, routes, environment variables, and high-impact files, and then guide follow-up reads with a compact project overview. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository scans can inspect broad project structure and surface environment variable references. <br>
Mitigation: Run it only on intended project roots and review generated context before sharing it outside the project team. <br>
Risk: Output and wiki modes can create local files. <br>
Mitigation: Confirm the destination path or mode before requesting saved output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-context-map) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown project context map with optional JSON output and local wiki files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an explicit output file or .codesight wiki articles when those modes are requested.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
