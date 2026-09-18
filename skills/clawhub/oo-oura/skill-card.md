## Description:

Oura enables agents to search and read Oura account data through an OOMOL-connected Oura connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to read Oura account data, including activity, readiness, sleep, SpO2, stress, resilience, heart rate, workouts, sessions, tags, ring data, and personal information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified internet installer commands.

Mitigation: Prefer verified manual installation or a pinned, signed oo CLI release before allowing the CLI to process sensitive health data.

Risk: The skill can access sensitive Oura health data through an OOMOL-connected account.

Mitigation: Confirm the requested records and account context before execution, keep credentials server-side through OOMOL, and fetch each action's live schema before sending payloads.

## Reference(s):

- [ClawHub Oura Skill](https://clawhub.ai/oomol/skills/oo-oura)
- [Oura Homepage](https://ouraring.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Oura Connection](https://console.oomol.com/app-connections?provider=oura)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before payload construction and returns Oura connector data through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
