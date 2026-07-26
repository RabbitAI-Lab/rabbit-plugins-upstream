## Description: <br>
LYGO mesh deploy supports Phase 5 epidemic gossip, SLM Merkle, mycelium, consensus routes, and Phase 9 TLS HTTPS node API workflows with local cluster scripts and pinned gossip before wide-area use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deepseekoracle](https://clawhub.ai/user/deepseekoracle) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to test and operate LYGO mesh deployments, including local HTTP convergence checks, TLS-enabled node API setup, and controlled wide-area mesh preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running cloned repository scripts can execute local code and start mesh node processes. <br>
Mitigation: Review scripts before execution, run them in an isolated workspace, and stop local clusters after testing. <br>
Risk: Public exposure of LYGO node API or wide-area mesh endpoints can create operational and security risk. <br>
Mitigation: Use TLS and pinned gossip before public internet use, and require explicit operator sign-off for wide-area deployment. <br>


## Reference(s): <br>
- [LYGO Protocol Stack GitHub Repository](https://github.com/DeepSeekOracle/lygo-protocol-stack) <br>
- [LYGO Protocol Stack Pages](https://deepseekoracle.github.io/lygo-protocol-stack/) <br>
- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-mesh-deploy) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local cluster operation commands, node API endpoint references, and TLS deployment guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
