## Description: <br>
x402 Compute helps agents browse, provision, manage, resize, extend, and destroy Singularity Cloud Network GPU/VPS instances, AI Machines, SGL Grid inference, and node-operator workflows using x402, MPP, or preloaded credits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivaavimusic](https://clawhub.ai/user/ivaavimusic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to provision paid GPU/VPS compute, deploy private OpenAI-compatible LLM endpoints, consume SGL Grid inference, or run grid nodes from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can spend wallet funds and manage cloud servers. <br>
Mitigation: Use a dedicated low-balance wallet, confirm spend and target instance before execution, and avoid unattended confirmation flags unless the cost and lifecycle action are known. <br>
Risk: The skill handles sensitive wallet keys, API keys, and root-access material. <br>
Mitigation: Keep secrets out of logs, prefer SSH keys over password fallback, delete any one-time password files immediately, and scope API keys to the intended workflow. <br>
Risk: Runtime installers or dependency changes can introduce supply-chain exposure. <br>
Mitigation: Pin or review dependencies and inspect the node installer before running remote install commands. <br>


## Reference(s): <br>
- [x402 Compute Documentation](https://docs.x402layer.cc/agentic-access/x402-compute) <br>
- [x402 Compute Cloud App](https://cloud.x402compute.cc) <br>
- [ClawHub Skill Page](https://clawhub.ai/ivaavimusic/skills/x402-compute) <br>
- [AI Machines Reference](references/ai-machines.md) <br>
- [x402Compute API Reference](references/api-reference.md) <br>
- [SGL Grid Node Operator Reference](references/node-operator.md) <br>
- [OpenWallet / OWS Reference](references/openwallet-ows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, environment-variable guidance, API request examples, and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands or configuration that manage paid cloud resources, wallet-backed payments, API keys, SSH access, and server lifecycle actions.] <br>

## Skill Version(s): <br>
1.10.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
