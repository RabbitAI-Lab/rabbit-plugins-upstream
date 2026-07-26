## Description: <br>
Virtual Intelligent Dev Team routes complex software tasks into bounded workflows with lead selection, optional copilots, verification, release gates, and resumable evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fxbin](https://clawhub.ai/user/fxbin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to triage complex software work, choose a lead workflow, and manage planning, implementation, iteration, release, and feedback loops with verifiable closure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository-changing commands, Git workflows, release gates, and /auto flows can affect a project workspace. <br>
Mitigation: Review generated plans first, confirm before running project scripts or commands, and use the setup and resume states for higher-risk work. <br>
Risk: Some referenced scripts or artifacts may not be included in the skill package. <br>
Mitigation: Verify referenced files exist before relying on a workflow path, and treat unavailable automation as guidance-only. <br>
Risk: Workflow routing advice can be incorrect or incomplete for a specific repository or release context. <br>
Mitigation: Require verifiable completion evidence, targeted checks, and human review before accepting done, ready, ship, or handoff claims. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fxbin/skills/virtual-intelligent-dev-team) <br>
- [Server-Resolved GitHub Provenance](https://github.com/fxbin/virtual-intelligent-dev-team) <br>
- [README](README.md) <br>
- [Usage Guide](docs/usage-guide.md) <br>
- [Playbook Index](references/playbook-index.md) <br>
- [Tooling Command Index](references/tooling-command-index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, command snippets, workflow bundles, and evidence summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose repository actions; review plans and commands before execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
