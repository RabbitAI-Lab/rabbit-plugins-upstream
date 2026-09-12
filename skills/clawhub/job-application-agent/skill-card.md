## Description:

Finds, evaluates, fills, submits, and tracks a candidate's own job applications using a verified resume, evidence-based targeting, secure local profile storage, and browser automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaibhavarora14](https://clawhub.ai/user/vaibhavarora14)

### License/Terms of Use:

MIT-0

## Use Case:

Candidates and their assisting agents use this skill to onboard or migrate a job-search profile, assess active roles, submit authorized applications, and track outcomes with application ledgers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic updater execution may run new skill code after installation.

Mitigation: Review the installed skill before use and disable automatic updates unless ongoing updates are explicitly desired.

Risk: Default identity analytics and community source sharing may send candidate identity or job metadata externally.

Mitigation: Disable telemetry identity sharing, telemetry, and community source sharing unless the candidate has reviewed and accepted those disclosures.

Risk: Routine-auto or continuing autonomy can submit applications without per-application review when authorization and eligibility conditions are met.

Mitigation: Use review-each by default and grant routine-auto or continuing autonomy only after confirming submission scope, destinations, and stored data behavior.

Risk: Durable retry behavior can continue trying to relay shared job metadata after transient failures.

Mitigation: Review and disable community sharing where persistent relay attempts are not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vaibhavarora14/skills/job-application-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured command inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local profile, resume, ledger, telemetry, source-sharing, attention, and friction records through its documented command workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
