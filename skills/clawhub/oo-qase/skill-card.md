## Description:

Qase (qase.io) support for reading, creating, and updating Qase data through the OOMOL-connected oo CLI instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to inspect Qase connector schemas, read Qase projects, test cases, and test runs, and create or complete Qase records through an OOMOL-connected account. It is intended for agents operating Qase on behalf of a user who has already configured the OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts for the oo CLI, which the security evidence identifies as avoidable high-impact installation risk.

Mitigation: Install only through a trusted OOMOL CLI distribution path, or manually download and verify the installer before execution.

Risk: The skill can create or complete Qase records through write actions.

Mitigation: Confirm the exact action payload and expected effect with the user before running write actions.

Risk: Qase data is handled through OOMOL's connected account flow.

Mitigation: Use the skill only when the user trusts OOMOL for the relevant Qase workspace and has configured the connection intentionally.

## Reference(s):

- [ClawHub Qase Skill](https://clawhub.ai/oomol/skills/oo-qase)
- [Qase Homepage](https://qase.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Qase connector schema inspection steps, JSON request payloads, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
