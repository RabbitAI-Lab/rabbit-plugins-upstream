## Description:

Routes new CTF challenges by category and directs the agent toward the appropriate solving workflow, setup checks, and first investigative commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Security learners, CTF participants, and developers use this skill to classify a new challenge, select the relevant specialty workflow, check their local solving environment, and identify initial commands while respecting event rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The environment check can print local Python, platform, tool, WSL, and common install-path information into the agent session.

Mitigation: Run the check only in sessions where that local environment information is acceptable to disclose.

Risk: The skill may route users toward offensive-security tools or CTF solving techniques that could conflict with competition or platform rules.

Mitigation: Review and follow the applicable CTF, training, or platform rules before using AI assistance or offensive-security tooling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxy050208/skills/ctf-router)
- [ClawHub publisher profile](https://clawhub.ai/user/yxy050208)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May suggest local environment checks and CTF tooling based on challenge type.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
