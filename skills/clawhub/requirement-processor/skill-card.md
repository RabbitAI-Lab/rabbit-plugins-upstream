## Description: <br>
Structured workflow for processing user requirements through analysis, documentation, phased planning, and iterative feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to clarify requested product or code changes, survey existing project context, produce a structured requirements document, confirm scope with the user, and plan implementation phases. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to read project files and create or update requirements documents, so inaccurate requirements could affect later implementation decisions. <br>
Mitigation: Review the generated requirements document with the user before implementation and keep changes limited to local Markdown planning artifacts until scope is confirmed. <br>
Risk: The release is a local requirements-planning workflow with no hidden execution, networking, credential, or background-worker behavior found in security evidence. <br>
Mitigation: Before installation, expect only local project reading and Markdown document writing for the stated workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bustes01/skills/requirement-processor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown requirements document and conversational planning guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local Markdown planning documents; no shell execution, network access, credentials, or background workers are expected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
