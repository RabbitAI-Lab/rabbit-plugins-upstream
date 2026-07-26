## Description: <br>
Intelligent skill orchestrator that compiles natural language requests into secure, reusable workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bvinci1-design](https://clawhub.ai/user/bvinci1-design) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation builders use Flow to turn natural-language build requests into composed reusable workflow skills, with registry search, security scanning, composition, and registration steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated workflow files and registry entries may be created from broad natural-language input without enough review controls. <br>
Mitigation: Install in an isolated environment, review generated files in the flows directory and skill_registry.json before running or reusing them, and consider disabling automatic registry updates. <br>
Risk: Dependencies are specified as broad version ranges, which can change installed behavior over time. <br>
Mitigation: Pin dependencies to reviewed safe versions before production use. <br>


## Reference(s): <br>
- [Flow ClawHub skill page](https://clawhub.ai/bvinci1-design/skills/flow) <br>
- [Flow README](README.md) <br>
- [Flow skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and console text with generated Python workflow files and JSON registry updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces generated files under the configured flows directory and can update skill_registry.json when automatic registry updates are enabled.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
