## Description: <br>
Designs and manages multi-step VMware workflows across companion skills with approval gates, state tracking, and rollback metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to plan, review, and coordinate multi-step VMware workflows such as incident response, clone-and-test changes, rolling maintenance, compliance scans, and cross-skill deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated workflow plans or custom YAML can lead to unsafe infrastructure changes if accepted without review. <br>
Mitigation: Review every generated plan and custom YAML before use, and require explicit approval before production changes. <br>
Risk: Rollback behavior should not be treated as a guaranteed automatic recovery mechanism. <br>
Mitigation: Treat rollback as a separate manual operation and maintain independent backout procedures for high-impact workflows. <br>
Risk: Companion skills may hold credentials or perform infrastructure actions outside the pilot skill itself. <br>
Mitigation: Restrict companion-skill credentials to least privilege and monitor local workflow, audit, template, and baseline files under ~/.vmware. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-pilot) <br>
- [VMware Pilot homepage](https://github.com/vmware-skills/VMware-Pilot) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Workflow Design Guide](references/workflow-design.md) <br>
- [Cross-Skill Integration Patterns](references/integration-patterns.md) <br>
- [Built-in Templates Reference](references/templates.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and YAML or JSON workflow snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Workflow plans and custom templates require human review before execution, especially for production infrastructure changes.] <br>

## Skill Version(s): <br>
1.8.8 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
