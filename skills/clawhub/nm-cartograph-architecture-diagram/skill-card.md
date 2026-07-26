## Description: <br>
Generates a Mermaid architecture diagram showing high-level component relationships. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to understand how plugins, modules, or codebase components relate to each other and to document those relationships for onboarding or review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated architecture diagrams may omit important components or misstate relationships if the explored scope is incomplete. <br>
Mitigation: Review the Mermaid diagram against the target codebase before using it for onboarding, documentation, or review decisions. <br>
Risk: Mermaid rendering or MCP output may fail or produce an inaccurate visualization when syntax is invalid. <br>
Mitigation: Validate the generated Mermaid flowchart and correct syntax errors before presenting the rendered result. <br>
Risk: Configured operational credentials or upload integrations can expose or persist incident data when directed by the user. <br>
Mitigation: Scope any configured credentials and review shared-memory or upload actions before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-cartograph-architecture-diagram) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with Mermaid flowchart code and a brief text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a Mermaid rendering MCP when available; rendering failures should be corrected and retried before presenting results.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter states 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
