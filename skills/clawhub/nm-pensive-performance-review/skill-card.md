## Description: <br>
Detects likely time and space complexity hotspots in project code using static analysis with optional enrichment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill before merges or during performance triage to scan target code paths for likely time and space complexity hotspots and receive ranked findings with suggested validation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Static-analysis findings may be false positives or may not reflect real runtime impact. <br>
Mitigation: Confirm important findings with profiling, benchmark reruns, or manual review before applying or claiming a performance fix. <br>
Risk: Optional gauntlet and kuva integrations may read additional project data or require separate tool installation. <br>
Mitigation: Review optional integrations and tool installs separately in environments with network, package, or source-code access restrictions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-performance-review) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report with inline code and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are informational and should be validated with profiling or benchmarks before fixes are treated as proven.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
