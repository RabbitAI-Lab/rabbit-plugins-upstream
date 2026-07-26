## Description: <br>
Maps file structure and module organization of a codebase for architecture reviews, refactoring planning, or migration scope estimation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to map repository structure, module boundaries, file distributions, and hotspots before architecture reviews, refactoring plans, or migration scoping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository mapping can expose directory names, filenames, and line-count details from the working tree. <br>
Mitigation: Run the skill only from the intended project directory and review or redact findings before sharing them. <br>
Risk: Broad file-structure scans can produce noisy or expensive results in large repositories. <br>
Mitigation: Scope the analysis root and exclude generated, dependency, virtual environment, and VCS directories where practical. <br>


## Reference(s): <br>
- [Nm Sanctum File Analysis on ClawHub](https://clawhub.ai/athola/skills/nm-sanctum-file-analysis) <br>
- [Sanctum homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown narrative with shell command examples and checklist status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Run from the intended project directory; no persistent output file is specified.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
