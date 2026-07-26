## Description: <br>
Create, validate, and publish Agent Skills following the official open standard from agentskills.io. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[killerapp](https://clawhub.ai/user/killerapp) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and engineers use this skill to create portable Agent Skills, validate their structure and metadata, convert existing documentation into skill packages, and prepare skills for use across agent tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Validator commands can fetch and run GitHub-hosted code locally. <br>
Mitigation: Use the validator only from trusted upstream sources, and pin it to a reviewed commit or release in sensitive environments. <br>
Risk: Generated skill templates may omit environment-specific safety details. <br>
Mitigation: Add permissions, external side effects, approval gates, verification steps, and rollback guidance before deployment. <br>


## Reference(s): <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>
- [Agent Skills Reference Repository](https://github.com/agentskills/agentskills) <br>
- [specification.md](references/specification.md) <br>
- [validation.md](references/validation.md) <br>
- [best-practices.md](references/best-practices.md) <br>
- [examples.md](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline YAML and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include skill templates, validation commands, troubleshooting guidance, and repository maintenance commands.] <br>

## Skill Version(s): <br>
2.5.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
