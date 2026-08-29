## Description:

Session retrospective and skill audit for reflecting on conversations, reviewing lessons learned, auditing what went well or wrong, and improving session effectiveness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ia-reflect to conduct structured retrospectives after a session, identify mistakes, friction, wins, and operational learnings, and decide which lessons should be persisted for future work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist approved retrospective lessons into local agent memory.

Mitigation: Review each proposed memory item before approving persistence, and avoid storing secrets, credentials, customer data, or sensitive personal/project information.

Risk: A retrospective or skill audit can produce incorrect or overly broad recommendations that affect future agent behavior.

Mitigation: Treat recommendations and proposed diffs as reviewable guidance, apply only concrete changes with clear evidence, and run the documented validation gates for skill edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [SKILL.md](SKILL.md)
- [SPEC.md](SPEC.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Code, Configuration]

**Output Format:** [Markdown with numbered recommendations, audit findings, proposed diffs, and memory-capture prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local memory updates and skill edits only after user review or approval.]

## Skill Version(s):

4.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
