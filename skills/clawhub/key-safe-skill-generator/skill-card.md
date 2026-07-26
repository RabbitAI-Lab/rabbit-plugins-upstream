## Description: <br>
A documentation-only meta-skill that teaches AI agents how to generate secure, zero-exposure skills using MGC Blackbox for credential management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zkeviny](https://clawhub.ai/user/zkeviny) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design credential-aware agent skills that keep secrets out of model prompts and route sensitive operations through local scripts or sealed runtime components. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the credential-safety guidance could expose secrets if an AI agent directly calls mgc_get for secret-bearing records or receives actual credentials in mgc_save content. <br>
Mitigation: Treat MGC identifiers as references only, keep credential retrieval inside local scripts or sealed runtime components, and return only non-sensitive operation results to the agent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zkeviny/skills/key-safe-skill-generator) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with templates, conceptual workflows, and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only output; generated skills should avoid exposing secrets to the agent and return only non-sensitive results.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter, manifest.json, and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
