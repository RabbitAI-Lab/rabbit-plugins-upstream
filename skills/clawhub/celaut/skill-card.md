## Description: <br>
Bridge skill for the Celaut decentralised-compute network: install the Celaut node, package projects into content-addressed microVM services, execute and observe workloads, and discover on-chain Unstoppable Skills through the read-only MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xf965](https://clawhub.ai/user/0xf965) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install and manage Celaut nodes, package services, estimate and execute decentralized workloads, monitor running microVMs, and query the Celaut Skills registry through MCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through privileged host setup and service management for a Celaut node. <br>
Mitigation: Install only on a controlled host, review installer content before running sudo commands, and verify downloaded binaries where possible. <br>
Risk: Wallet mnemonics and Ergo payments are sensitive, and payment transactions are final. <br>
Mitigation: Keep mnemonics out of shared workspaces, avoid exposing wallet configuration, and require explicit operator confirmation before payment or reputation actions. <br>
Risk: Observe features can expose workload metrics and packet-level network activity. <br>
Mitigation: Restrict observe and Gateway.Observe access to trusted operators and avoid collecting captures unless needed. <br>
Risk: Uninstall and directory-management guidance can remove important local files if pointed at the wrong path. <br>
Mitigation: Double-check TARGET_DIR and effective config paths before uninstalling or deleting node directories. <br>


## Reference(s): <br>
- [Celaut Paradigm](https://github.com/celaut-project/paradigm) <br>
- [Nodo Repository](https://github.com/celaut-project/nodo) <br>
- [Nodo Configuration Example](https://github.com/celaut-project/nodo/blob/stable/config.example.yaml) <br>
- [Celaut Skills Registry](https://github.com/celaut-project/skills) <br>
- [Celaut Skills MCP Specification](https://github.com/celaut-project/skills/blob/main/MCP.md) <br>
- [Ergo Manifesto](https://ergoplatform.org/en/blog/2021-04-26-the-ergo-manifesto/) <br>
- [ClawHub Skill Page](https://clawhub.ai/0xf965/skills/celaut) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include privileged host-management commands and operational cautions; the skill guides agent actions rather than directly executing them.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
