## Description: <br>
Audits Makefiles for build correctness, portability, and recipe duplication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and build engineers use this skill before committing Makefile changes, CI/CD updates, or build-system refactors to identify dependency, portability, duplication, and target-coverage issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move from review into broad Makefile modification when apply-style workflows are used. <br>
Mitigation: Review all proposed Makefile edits before allowing apply workflows, especially changes that affect CI, release, install, cleanup, or recursive target behavior. <br>
Risk: Generated or suggested Makefile targets can alter project automation behavior. <br>
Mitigation: Run dry-run or syntax checks such as make -n on affected targets and compare the working tree diff before committing changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-makefile-review) <br>
- [Project homepage from metadata](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown review report with findings, file references, command snippets, and recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include suggested Makefile target changes; review proposed edits before applying them.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
