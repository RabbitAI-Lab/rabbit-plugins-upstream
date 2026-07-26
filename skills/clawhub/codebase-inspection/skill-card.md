## Description: <br>
Advanced codebase analysis with HTML reports, git-aware diffs, trend tracking, SVG badges, CSV export, and CI/CD integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering leads, maintainers, and CI pipelines use this skill to inspect local codebases, measure language and line-count trends, generate reports, compare snapshots, and surface badges for project status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The main metrics tool reads local directories and can write report or snapshot files. <br>
Mitigation: Run it only on directories you are comfortable letting it read, and choose report or snapshot output paths deliberately. <br>
Risk: The bundled CI verifier can automatically run Python files from a target folder. <br>
Mitigation: Do not run ci/verify_product.py against untrusted repositories or submissions unless it is inside a disposable sandbox with no secrets and limited filesystem and network access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/codebase-inspection) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, csv, html, svg, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples; tool output can be plain text, JSON, CSV, HTML report files, SVG badges, or trend snapshots.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operates on local directories; optional output paths control HTML reports and snapshots.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
