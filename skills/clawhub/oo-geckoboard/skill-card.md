## Description: <br>
Enables agents to operate Geckoboard datasets through the OOMOL oo CLI, including schema inspection and dataset create, append, replace, and delete actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent inspect the live Geckoboard connector contract and run dataset operations through an OOMOL-connected account. It is suited to maintaining operational dashboards where records may need to be appended, replaced, created, or deleted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The append_dataset_data action changes Geckoboard data but is not tagged as a write action in the skill text. <br>
Mitigation: Treat append_dataset_data as a write action and confirm the target dataset, records, and update behavior before execution. <br>
Risk: Dataset operations can replace or delete important dashboard data. <br>
Mitigation: Require explicit user confirmation for replace_dataset_data and delete_dataset, including the dataset identifier and expected effect. <br>
Risk: Use depends on the external oo CLI, OOMOL account state, connected Geckoboard credentials, and available billing credit. <br>
Mitigation: Review the oo CLI setup and OOMOL connection requirements before installing, and resolve authentication, scope, credential, or billing errors before retrying actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-geckoboard) <br>
- [Geckoboard homepage](https://www.geckoboard.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return JSON from the oo CLI, including data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence, release metadata, and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
