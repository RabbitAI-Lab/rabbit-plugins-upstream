## Description: <br>
Audits Makefiles for build correctness, portability, and recipe duplication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review Makefile changes, map dependencies, identify duplicated recipes, check portability, and summarize recommended follow-up actions before committing build-system changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run Make-related validation commands against repository files. <br>
Mitigation: Use it in a trusted or sandboxed repository, review proposed commands first, and avoid executing generated Make targets from untrusted projects. <br>
Risk: The plugin dogfood workflow can apply generated build targets when an --apply flow is used. <br>
Mitigation: Require a diff and explicit confirmation before applying changes, then review modified Makefiles before committing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-makefile-review) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with findings, context, dependency analysis, duplication candidates, portability issues, missing targets, and a recommendation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Makefile target suggestions and command outputs with file and line references.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
