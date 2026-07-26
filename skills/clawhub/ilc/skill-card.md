## Description: <br>
Evidence-first graph protocol for human-AI truth maintenance, attribution, CCSS contact, and OpenClaw local graph work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jamison](https://clawhub.ai/user/jamison) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and operators use this skill to find the canonical ILC source, install the public-RC CLI, initialize local identity, submit local truth primitives, inspect status records, and contact Genesis through CCSS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the ILC source package runs code outside this skill artifact. <br>
Mitigation: Review the linked ILC repository before installation and install in a controlled environment appropriate for external CLI code. <br>
Risk: Identity, local graph, and CCSS messaging commands can create persistent protocol setup actions. <br>
Mitigation: Use a deliberate workspace, inspect the command behavior, and confirm user intent before identity setup, graph submission, or CCSS messaging. <br>
Risk: Public-RC status leaves mainnet, production minting, live settlement, wallet writes, public P2P activation, and epoch transition inactive. <br>
Mitigation: Treat those production actions as unavailable unless a later authoritative gate record says otherwise. <br>


## Reference(s): <br>
- [ILC ClawHub listing](https://clawhub.ai/jamison/skills/ilc) <br>
- [ILC source repository](https://github.com/jamison/ilc) <br>
- [README](https://github.com/jamison/ilc/blob/main/README.md) <br>
- [Human introduction](https://github.com/jamison/ilc/blob/main/HUMANS.md) <br>
- [Whitepaper](https://github.com/jamison/ilc/blob/main/WHITEPAPER.md) <br>
- [Quickstart](https://github.com/jamison/ilc/blob/main/QUICKSTART.md) <br>
- [Economics](https://github.com/jamison/ilc/blob/main/economics.md) <br>
- [Operator setup](https://github.com/jamison/ilc/blob/main/docs/GETTING_STARTED.md) <br>
- [Public RC gate](https://github.com/jamison/ilc/blob/main/docs/specs/ilc_public_rc_gate_001_1575c_v0.1.md) <br>
- [Genesis contact protocol](https://github.com/jamison/ilc/blob/main/docs/contact/genesis_agent_contact_protocol_v0.1.md) <br>
- [CCSS contacts](https://github.com/jamison/ilc/blob/main/docs/contact/ccss_contacts.json) <br>
- [OpenClaw local capture implementation](https://github.com/jamison/ilc/blob/main/skills/ilc-openclaw-local-capture/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and reference links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external ilc binary for CLI workflows.] <br>

## Skill Version(s): <br>
0.4.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
