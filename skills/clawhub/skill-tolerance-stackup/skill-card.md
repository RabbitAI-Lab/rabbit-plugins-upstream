## Description: <br>
Helps dimensional, process, and design engineers perform one-dimensional tolerance stack-up analysis with Worst Case and Root Sum Square methods, validate assembly gap or interference requirements, and identify tolerance contributors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Engineers use this skill to calculate and compare WC and RSS tolerance stack-ups for linear dimension chains, then check whether the resulting clearance or interference satisfies assembly requirements. It is also useful for tolerance allocation, overrun contributor analysis, process dimension chains, and basic GD&T-to-linear-stackup discussions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tolerance-stackup outputs can be misleading if assumptions such as independent normal distributions, symmetric tolerances, or GD&T-to-linear conversions do not match the user's engineering standards. <br>
Mitigation: Verify assumptions, requirement limits, Cpk/process capability expectations, and GD&T conversion rules with qualified engineering reviewers before using results for production design decisions. <br>
Risk: The artifact text references report-generation scripts, but the release evidence states there is no packaged executable code. <br>
Mitigation: Treat script references as workflow guidance only, and do not run any local script unless its source is available, reviewed, and scanned in the deployment environment. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-tolerance-stackup) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-tolerance-stackup) <br>
- [Publisher profile](https://clawhub.ai/user/duding-engicool) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Text, Guidance] <br>
**Output Format:** [Plain text and Markdown calculation reports with formulas, tables, requirement checks, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided dimension-chain inputs, tolerances, direction signs, and assembly requirements; results should be reviewed against company standards before production use.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
