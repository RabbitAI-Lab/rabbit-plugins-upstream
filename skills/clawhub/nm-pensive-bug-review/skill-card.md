## Description: <br>
Systematically identifies, documents, fixes, and verifies software bugs with evidence trails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review code for defects, reproduce issues, document root causes, prepare minimal fixes, and produce verification evidence before releases, audits, or merges. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers may activate the workflow during routine development requests. <br>
Mitigation: Confirm that bug review is the intended task before letting the agent inspect files, run verification commands, or prepare changes. <br>
Risk: Suggested fixes or tests may be incorrect or incomplete for the target project. <br>
Mitigation: Review proposed code changes, run the documented verification commands locally, and keep normal code review gates in place. <br>
Risk: Expertise-style wording can overstate authority. <br>
Mitigation: Treat persona language as review framing and verify findings against project evidence, tests, and maintainer judgment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-bug-review) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with defect findings, proposed code changes, test updates, evidence notes, and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include file and line references, severity labels, root cause summaries, verification commands, and remaining risk notes.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
