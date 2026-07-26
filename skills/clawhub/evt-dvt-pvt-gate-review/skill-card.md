## Description: <br>
Runs an NPI phase-gate review for EVT, DVT, or PVT by scoring exit criteria, triaging open issues, reading yield, tracking waivers, and producing a go/conditional-go/no-go recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hardware NPI teams and product engineers use this skill to structure EVT, DVT, or PVT gate reviews from build results, open issues, exit criteria, yield data, waivers, and schedule pressure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive build, yield, defect, or schedule data may be included in user-provided gate review inputs. <br>
Mitigation: Review and minimize sensitive program data before sharing it with an agent. <br>
Risk: Incomplete gate evidence can lead to an unsupported pass recommendation. <br>
Mitigation: Mark missing criteria as no-data and require explicit owners, expiry, and containment for waivers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/evt-dvt-pvt-gate-review) <br>
- [Publisher profile](https://clawhub.ai/user/mohitagw15856) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/evt-dvt-pvt-gate-review.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown gate review document with scorecards, triage tables, yield readouts, waiver registers, and a recommendation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided program data; missing criteria should be marked no-data rather than assumed pass.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
