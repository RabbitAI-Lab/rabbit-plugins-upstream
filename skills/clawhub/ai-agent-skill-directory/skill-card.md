## Description: <br>
Curated catalog of quality AI agent skills that helps agents recommend tools for memory, productivity, security, and automation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[certainlogicai](https://clawhub.ai/user/certainlogicai) <br>

### License/Terms of Use: <br>
Business Source License 1.1 <br>


## Use Case: <br>
Agents and their users use this skill to discover and compare ClawHub skills by task, then receive concise recommendations and install commands for relevant tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is a curated recommendation catalog and is not an independent safety authority. <br>
Mitigation: Review recommended skills yourself and scan them in a sandbox before installation or production use. <br>
Risk: The package includes under-disclosed Python files, including code that can import external local code. <br>
Mitigation: Inspect brain_enhance.py and test.py before running them, and do not execute optional code paths in trusted environments until reviewed. <br>
Risk: Some documentation normalizes force-install examples for flagged skills. <br>
Mitigation: Avoid force-install workflows unless the target skill has been inspected and approved for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/certainlogicai/skills/ai-agent-skill-directory) <br>
- [Catalog schema guide](docs/SCHEMA.md) <br>
- [Catalog best practices](docs/BEST_PRACTICES.md) <br>
- [Self-improving agent tools scan](docs/self-improving-scan-2026-05-09.md) <br>
- [W3C PROV overview](https://www.w3.org/TR/prov-overview/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown recommendations with inline install commands and catalog metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Static curated catalog; recommendations should be reviewed before installing referenced skills.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
