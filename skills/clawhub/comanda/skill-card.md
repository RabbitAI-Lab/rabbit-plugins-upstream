## Description: <br>
Generate, visualize, and execute declarative AI pipelines using the comanda CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kris-hansen](https://clawhub.ai/user/kris-hansen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, inspect, edit, and run Comanda YAML workflows for multi-model LLM pipelines, shell-assisted tool steps, branching, batching, and agentic loops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or edited YAML workflows may contain incorrect data flow, model choices, file paths, or execution settings. <br>
Mitigation: Review generated YAML and validate non-trivial workflows with comanda chart before running comanda process. <br>
Risk: Shell-enabled workflow steps can run local commands when trusted workflows permit tool use. <br>
Mitigation: Run only trusted workflows, keep tool allowlists narrow, prefer read-only commands, and avoid untrusted shell-enabled workflows. <br>
Risk: Workflows that index private repositories or run long agentic loops can expose sensitive context or continue automation longer than intended. <br>
Mitigation: Scope API keys and file access, review indexed content before use, and monitor or cancel long-running loops when needed. <br>


## Reference(s): <br>
- [Comanda homepage](https://comanda.sh) <br>
- [Comanda Workflow Spec](references/WORKFLOW-SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include workflow file paths, CLI flags, model identifiers, tool allowlists, and validation or troubleshooting commands.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
