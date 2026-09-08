## Description:

Evidence-first graph protocol for human-AI truth maintenance, attribution, CCSS contact, and OpenClaw local graph work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jamison](https://clawhub.ai/user/jamison)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to install and operate the public-RC ILC CLI for local graph work, agent identity setup, truth primitive submission, public-RC status inspection, and Genesis CCSS contact handling with fallback email while D2D delivery remains inactive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source installation runs public repository Python package code under the user's account.

Mitigation: Install only from a trusted reviewed source, prefer pinning a specific commit, and use an isolated virtual environment without sensitive credentials.

Risk: CCSS send or contact commands may transmit message content and metadata as outbound communication.

Mitigation: Review CCSS command intent and message contents before sending; use fallback email only when appropriate for live correspondence.

Risk: The public-RC status keeps mainnet, production minting, live settlement, wallet writes, public P2P activation, and epoch transition inactive until later gate records authorize them.

Mitigation: Treat public-RC workflows as source installation, local graph work, documentation, sidecar inspection, and guarded rehearsal unless a later signed gate record changes the status.

## Reference(s):

- [ClawHub ILC Skill](https://clawhub.ai/jamison/skills/ilc)
- [Canonical ILC Source](https://github.com/jamison/ilc)
- [ILC README](https://github.com/jamison/ilc/blob/main/README.md)
- [ILC Quickstart](https://github.com/jamison/ilc/blob/main/QUICKSTART.md)
- [Public RC Gate](https://github.com/jamison/ilc/blob/main/docs/specs/ilc_public_rc_gate_001_1575c_v0.1.md)
- [Genesis Contact Protocol](https://github.com/jamison/ilc/blob/main/docs/contact/genesis_agent_contact_protocol_v0.1.md)
- [OpenClaw Local Capture Implementation](https://github.com/jamison/ilc/blob/main/skills/ilc-openclaw-local-capture/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell command blocks and linked references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the ilc CLI binary and Python 3.10+ source-install workflow described by the skill.]

## Skill Version(s):

0.4.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
