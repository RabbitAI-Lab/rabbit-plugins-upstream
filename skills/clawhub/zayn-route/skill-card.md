## Description: <br>
分析复杂职场问题，判断应先使用哪个 Skill，并规划调用顺序、参数传递、停止条件和最终输出 Skill。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and operators use this skill to decide whether a workplace request should be handled by one skill or by a short sequence of skills. It plans routing order, required inputs, handoff fields, stop conditions, and the final output skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat routing recommendations as permission to execute downstream business actions. <br>
Mitigation: Confirm any high-impact follow-up skill before execution; the router recommends sequence and inputs but does not complete the downstream action itself. <br>
Risk: Incomplete or conflicting inputs can lead to premature downstream skill recommendations. <br>
Mitigation: Stop routing when key parameters are missing or conflicting, list the missing information, and resume from the appropriate skill only after clarification. <br>
Risk: A simple request may be over-orchestrated into an unnecessary multi-skill chain. <br>
Mitigation: Check whether one skill is sufficient before recommending a chain, and keep chains to five or fewer skills unless the need is explicit. <br>
Risk: Unverified assumptions may be passed to downstream skills as facts. <br>
Mitigation: Pass only necessary fields, preserve conflict and verification labels, and identify the source skill for handoff content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-route) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown tables and concise routing recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter status, recommended skill chain, handoff notes, stop conditions, and final output skill.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
