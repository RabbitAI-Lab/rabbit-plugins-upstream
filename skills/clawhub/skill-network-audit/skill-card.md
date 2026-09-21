## Description:

Skill Network Audit helps agents inspect ClawPhylax ledger evidence for installed skills, reporting observed network hosts, flagged events, uploads, credential reads, blocked requests, and witness-card summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeneassoft](https://clawhub.ai/user/aeneassoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to ask an agent where an installed skill or tool sent data at runtime. The skill guides the agent to query the local ClawPhylax ledger, report only observed host activity, and distinguish unobserved behavior from safety claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide user-approved allow or deny changes to host policy.

Mitigation: Review each proposed allow or deny change before approving it, especially because enforcement mode can interrupt tasks.

Risk: Ledger evidence may be incomplete when a skill has not run or has too little history.

Mitigation: Report absent activity as not observed yet, preserve the learning or stable baseline, and avoid treating no events as a safety finding.

Risk: Process attribution has limits for shell commands and child processes.

Mitigation: State the attribution limits plainly and rely on exact skill-path attribution only when the command path contains the relevant skills directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aeneassoft/skills/skill-network-audit)
- [Project homepage](https://github.com/aeneassoft/clawphylax)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should be limited to what the local ledger shows and should avoid claiming a skill is safe when no events have been observed.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
