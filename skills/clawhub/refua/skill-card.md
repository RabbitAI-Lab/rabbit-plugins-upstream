## Description: <br>
Fold and score biomolecular complexes and optionally profile ADMET to prioritize molecules in drug discovery pipelines via the refua-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jbenjoseph](https://clawhub.ai/user/jbenjoseph) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and drug discovery practitioners use Refua to fold and score protein-ligand, protein-protein, and fold-only DNA/RNA complexes, estimate binding affinity, and optionally run ADMET predictions through a local MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local package installs, model downloads, MCP server execution, and model caches may expose sensitive molecular inputs if the runtime or packages are not trusted. <br>
Mitigation: Install Refua only in a trusted virtual environment or container, verify the refua and refua-mcp package sources, and review logging and cache behavior before submitting confidential molecular structures. <br>


## Reference(s): <br>
- [Refua ClawHub release](https://clawhub.ai/jbenjoseph/skills/refua) <br>
- [refua-mcp repository](https://github.com/agentcures/refua-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require local Refua and refua-mcp packages, model downloads, CPU or GPU resources, and optional ADMET extras.] <br>

## Skill Version(s): <br>
0.4.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
