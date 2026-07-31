## Description: <br>
Audits an AI agent's local setup, including workspace, configuration, memory, skills, jobs, integrations, exposure, cost, and reliability issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect an agent's own local operating environment before trusting it with new work, diagnosing failures, or reducing exposure, cost, and reliability drift. It produces evidence-backed findings and proposed remediations for local agent setup issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill inspects sensitive local setup areas, including configuration, credential locations, sessions, schedules, and local notes. <br>
Mitigation: Install it only when local self-audit is desired; it stores local notes only under declared Clawic data paths and records credential pointers rather than credential values. <br>
Risk: Audit output could expose sensitive details if credential values or private content are quoted in reports. <br>
Mitigation: The skill directs findings to name file, line, and credential kind only, and to avoid printing, copying, transmitting, or storing credential values. <br>
Risk: Automatic fixes could change local files, sessions, history, or credentials in ways the user did not intend. <br>
Mitigation: Keep the default proposal-only autofix posture; destructive actions require explicit confirmation, a stated blast radius, an inverse, and verification. <br>
Risk: Authenticated integration checks could consume quota or touch external services unnecessarily. <br>
Mitigation: Use local evidence first and make authenticated calls only to already configured services when the question cannot be answered locally, at most once per integration per run. <br>


## Reference(s): <br>
- [ClawHub Analysis skill page](https://clawhub.ai/ivangdavila/skills/analysis) <br>
- [Clawic Analysis skill page](https://clawic.com/skills/analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with evidence, severity labels, proposed actions, and local note updates when durable findings are recorded.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings are grouped by severity, capped for readability, and avoid reproducing credential values.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
