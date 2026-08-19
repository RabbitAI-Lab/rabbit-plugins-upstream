## Description:

Capability Decay Watchdog monitors skill learned_patterns.json health data for success-rate drops or stale activity and reports alerts with suggested repair, learner injection, or regression actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to monitor local skill-health records, detect capability decay or stale skills, and produce suggested self-healing actions before failures become visible in normal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learning records can contain notes, errors, and preferences saved as plaintext JSON.

Mitigation: Do not record secrets, credentials, private user data, or sensitive incident details in learner notes, errors, or preferences.

Risk: Health checks depend on available learned_patterns.json metrics and may miss skills that do not record learner data consistently.

Mitigation: Ensure monitored skills call the learner consistently and pair watchdog alerts with regression checks before repair or release decisions.

Risk: The watchdog reports operational decay signals but does not prove that a skill's logic remains correct.

Mitigation: Use the alerts as triage signals and validate suspected decay with targeted tests or review before making changes.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON reports with alert records and recommended actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No external dependencies; reads local learned_patterns.json files under a skills directory.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
