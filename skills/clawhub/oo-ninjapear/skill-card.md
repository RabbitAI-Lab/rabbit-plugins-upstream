## Description:

NinjaPear (nubela.co) lets an agent inspect NinjaPear action schemas and run company research, email classification, and account credit lookup actions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected NinjaPear account use this skill to retrieve company intelligence, check email provider status, look up company websites, and inspect account credit balance without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad oo CLI command authority relative to its NinjaPear lookup purpose.

Mitigation: Review before installing, install oo from verified official documentation, and allow only requested NinjaPear connector actions.

Risk: First-time setup can involve installing or authenticating the oo CLI.

Mitigation: Do not let the skill perform first-time installation or unrelated oo commands automatically; run setup steps only after an auth or connection failure requires them.

## Reference(s):

- [ClawHub NinjaPear Skill Page](https://clawhub.ai/oomol/skills/oo-ninjapear)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [NinjaPear Homepage](https://nubela.co/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented NinjaPear connector actions through the oo CLI after inspecting live action schemas.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
