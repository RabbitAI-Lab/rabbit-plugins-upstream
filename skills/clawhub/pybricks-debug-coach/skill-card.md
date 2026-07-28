## Description: <br>
Coach Pybricks and LEGO robot debugging through evidence, one-variable tests, and observable pass/fail checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aimasterhao](https://clawhub.ai/user/aimasterhao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Learners, mentors, educators, and developers use this skill to debug Pybricks and LEGO robot issues from supplied tracebacks, code excerpts, observations, robot mappings, and telemetry. It helps identify the earliest mismatch, name one evidence-supported likely cause, and propose one controlled experiment with observable pass/fail checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Debugging evidence could include secrets, private files, confidential data, or identifying information about children. <br>
Mitigation: Provide only non-identifying code excerpts, logs, telemetry, and robot descriptions; omit secrets, private files, names, faces, voices, schools, and contact details. <br>
Risk: A proposed robot test could be unsafe if the robot configuration, attachment clearance, surface, or nearby people are not accounted for. <br>
Mitigation: Stop before motion when safety context is unclear, keep tests small and observable, and avoid moving unknown hardware without a safety check. <br>
Risk: The skill can give misleading coaching when supplied telemetry, Hub details, firmware version, or port mapping are incomplete. <br>
Mitigation: Treat missing data as an evidence gap and collect the smallest useful observation before changing code or hardware. <br>


## Reference(s): <br>
- [Project repository](https://github.com/aiMasterHao/pybricks-debug-coach) <br>
- [Official Pybricks documentation](https://docs.pybricks.com/) <br>
- [Structured output contract](references/contracts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown sections for normal conversation, or one JSON object when structured output is requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill analyzes only caller-supplied evidence and does not directly connect to, upload to, run, or collect telemetry from LEGO hubs.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence and changelog, released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
