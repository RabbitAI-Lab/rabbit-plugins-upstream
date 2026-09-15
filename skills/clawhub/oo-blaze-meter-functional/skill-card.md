## Description:

BlazeMeter Functional lets an agent use the OOMOL-connected oo CLI to search and read BlazeMeter Functional data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and external users use this skill to list BlazeMeter Functional multi-tests, retrieve multi-test details, and report active sessions through an OOMOL-managed connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code on a user's machine.

Mitigation: Do not run curl|bash or irm|iex installer commands automatically; prefer an official, versioned installation path with checksum or signature verification after reviewing what it changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blaze-meter-functional)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [BlazeMeter Functional homepage](https://www.blazemeter.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions are read-oriented in the provided artifact; live action schemas are inspected before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
