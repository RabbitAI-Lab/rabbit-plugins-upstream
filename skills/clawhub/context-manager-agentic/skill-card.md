## Description: <br>
Verify and distribute trust-gated context (memory and skill files) to a multi-agent roster before it's injected. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tryboy869](https://clawhub.ai/user/tryboy869) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to assemble scoped context bundles for multiple agents while distinguishing hash-verified instruction sources from untrusted reference material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local memory and skill files and writes local audit records, so it may package sensitive context if pointed at broad or confidential directories. <br>
Mitigation: Review configured directories before use and provide only memory or skill locations whose contents are appropriate to distribute to agents. <br>
Risk: Untrusted or modified context could be mistaken for agent instructions if downstream workflows ignore the skill's trust labels. <br>
Mitigation: Preserve trust tags in distributed bundles and treat unverified content as reference material rather than executable instruction. <br>
Risk: The release is a third-party ClawHub skill with external project documentation. <br>
Mitigation: Review the referenced project and npm dependency before installation, as recommended by the server security guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tryboy869/skills/context-manager-agentic) <br>
- [Project documentation](https://github.com/Tryboy869/context-manager-agentic) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and git according to server-resolved metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
