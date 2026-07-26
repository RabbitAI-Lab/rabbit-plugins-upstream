## Description: <br>
BOOK BRAIN is a LYGO 3-Brain filesystem helper for scaffolding memory, reference, and state layouts, writing outer reference stubs, and maintaining daily indexes with an additive-only workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to organize OpenClaw, ClawHub Haven, LYGO, and Builder Key workspaces into durable memory, reference, state, log, tool, and scratch areas. It helps propose additive scaffolds, write reference stubs, and maintain indexes for long-horizon retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update local memory, reference, state, log, tool, and scratch files in a user-selected workspace. <br>
Mitigation: Review dry-run plans before applying changes and use explicit workspace paths. <br>
Risk: Generated memory notes and reference stubs may accidentally capture sensitive material if users provide it. <br>
Mitigation: Do not store API keys, tokens, .env values, wallet seeds, private keys, or secret-bearing webhook URLs in generated notes or stubs. <br>
Risk: Optional paired lyra-brain or lattice helper commands may expand the workflow beyond this skill's local filesystem helper behavior. <br>
Mitigation: Require separate approval before running paired skill or lattice helper commands. <br>


## Reference(s): <br>
- [BOOK BRAIN security guidance](references/SECURITY.md) <br>
- [BOOK BRAIN agent contract](references/AGENT_CONTRACT.md) <br>
- [BOOK BRAIN and LYRA memory layout](references/MEMORY_LAYOUT.md) <br>
- [BOOK BRAIN LYGO lattice integration](references/LATTICE_INTEGRATION.md) <br>
- [BOOK BRAIN examples and patterns](references/book-brain-examples.md) <br>
- [ClawHub LYGO stack reference](reference/CLAWHUB_LYGO_STACK.ref.txt) <br>
- [BOOK BRAIN ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/book-brain) <br>
- [deepseekoracle ClawHub publisher profile](https://clawhub.ai/user/deepseekoracle) <br>
- [LYGO protocol stack pages](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON dry-run plans, and generated filesystem files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for additive workspace organization; file writes should follow dry-run review and avoid secrets.] <br>

## Skill Version(s): <br>
2.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
