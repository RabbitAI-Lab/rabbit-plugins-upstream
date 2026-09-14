## Description:

Evidence-first graph protocol for human-AI truth maintenance, attribution, CCSS contact, and OpenClaw local graph work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jamison](https://clawhub.ai/user/jamison)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agents use this skill to install and route through the ILC CLI, enroll with an invite, initialize local agent identity, and submit or inspect local graph work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and run the third-party ILC CLI, which may create local identity and enrollment state.

Mitigation: Use an isolated virtual environment, review the upstream repository and installer, and provide invite or identity material only when the ILC project and package distribution path are trusted.

Risk: The artifact describes a public-RC state where mainnet, production minting, live settlement, wallet writes, public P2P activation, and epoch transition remain inactive.

Mitigation: Treat the workflow as invite-gated local graph and guarded rehearsal work unless a later signed gate record authorizes broader activation.

## Reference(s):

- [ClawHub ilc listing](https://clawhub.ai/jamison/skills/ilc)
- [ILC source repository](https://github.com/jamison/ilc)
- [README](https://github.com/jamison/ilc/blob/main/README.md)
- [Human introduction](https://github.com/jamison/ilc/blob/main/HUMANS.md)
- [Whitepaper](https://github.com/jamison/ilc/blob/main/WHITEPAPER.md)
- [Quickstart](https://github.com/jamison/ilc/blob/main/QUICKSTART.md)
- [Economics](https://github.com/jamison/ilc/blob/main/economics.md)
- [Operator setup](https://github.com/jamison/ilc/blob/main/docs/GETTING_STARTED.md)
- [Public RC gate](https://github.com/jamison/ilc/blob/main/docs/specs/ilc_public_rc_gate_001_1575c_v0.1.md)
- [Genesis contact protocol](https://github.com/jamison/ilc/blob/main/docs/contact/genesis_agent_contact_protocol_v0.1.md)
- [CCSS contacts](https://github.com/jamison/ilc/blob/main/docs/contact/ccss_contacts.json)
- [OpenClaw local capture implementation](https://github.com/jamison/ilc/blob/main/skills/ilc-openclaw-local-capture/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the ilc CLI binary for the documented workflows.]

## Skill Version(s):

0.5.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
