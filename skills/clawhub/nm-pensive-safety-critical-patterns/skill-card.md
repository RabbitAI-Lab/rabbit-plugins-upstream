## Description: <br>
Applies NASA Power of 10 rules for safety-critical verifiable code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and code reviewers use this skill to apply higher-rigor safety-critical coding review patterns to financial, medical, data-integrity, and other high-reliability software. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be used to guide changes in safety-critical or high-reliability code where incorrect advice could have meaningful impact. <br>
Mitigation: Require human review, tests, and domain-specific verification before applying suggested patterns to production code. <br>
Risk: The referenced external pensive plugin may add agents, hooks, or commands that are not present in this markdown-only skill. <br>
Mitigation: Review and scan the external plugin separately before installing or enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-safety-critical-patterns) <br>
- [Pensive plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown guidance with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no commands are run by the skill itself.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
