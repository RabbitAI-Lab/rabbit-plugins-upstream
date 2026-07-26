## Description: <br>
Audits shell scripts for correctness, portability, and common pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review shell scripts used in CI/CD pipelines, hooks, wrappers, build automation, and pre-commit workflows. It focuses the review on exit-code propagation, portability, safety patterns, script structure, and evidence-backed findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad shell and CI activation terms may cause the skill to be invoked during general shell-script discussions. <br>
Mitigation: Confirm the review target and scope before applying recommendations. <br>
Risk: The skill may suggest copyable commands, including commands that format files in place or invoke package managers. <br>
Mitigation: Inspect commands before running them and prefer read-only checks or dry runs before applying changes. <br>
Risk: Review guidance may be incomplete or incorrect for a specific repository or shell dialect. <br>
Mitigation: Validate findings with ShellCheck, relevant tests, and human review before relying on the recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-shell-review) <br>
- [Pensive source homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>
- [Exit Code Patterns](modules/exit-codes.md) <br>
- [Shell Portability](modules/portability.md) <br>
- [Shell Safety Patterns](modules/safety-patterns.md) <br>
- [Shell Script Structure Patterns](modules/structure-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review findings with script lists, issue sections, suggested fixes, and an approval recommendation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include copyable discovery, verification, and formatting commands; inspect commands before running them.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
