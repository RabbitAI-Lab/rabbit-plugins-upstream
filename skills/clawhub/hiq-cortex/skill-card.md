## Description: <br>
Looks up LCA emission factors, carbon footprint data, published EPDs, and benchmark distributions from HiQ Cortex and related life-cycle inventory sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kirbyingithub](https://clawhub.ai/user/kirbyingithub) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
LCA practitioners, sustainability teams, and developers use this skill to retrieve tool-backed emission factors, product carbon footprints, BOM accounting inputs, production-route comparisons, EPD peer checks, and industry benchmarks with stated database, version, model, geography, and unit basis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LCA search terms and dataset keys are sent to HiQ Cortex during use. <br>
Mitigation: Install only when that data sharing is acceptable, and avoid including confidential project identifiers in search terms unless approved. <br>
Risk: Access requires an API key, browser-login credential, or MCP configuration that can grant data access. <br>
Mitigation: Prefer environment variables or the documented login flow, review MCP config changes before retaining them, and run logout or remove credentials and config entries when access is no longer needed. <br>
Risk: Emission factors can be misleading when compared across incompatible units, system models, geographies, database versions, or system boundaries. <br>
Mitigation: Report the basis with every value and decline direct comparisons when functional unit, system model, geography, database version, or boundary are not comparable. <br>
Risk: Restricted commercial datasets may be unavailable to the current account. <br>
Mitigation: Surface entitlement restrictions and purchase links truthfully, and label any free-database alternative as a substitute rather than silently replacing restricted data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kirbyingithub/skills/hiq-cortex) <br>
- [ClawHub Homepage Metadata](https://github.com/HiQ-AI/agent-skills) <br>
- [HiQ Data](https://www.hiqlcd.com/) <br>
- [Comparability](references/comparability.md) <br>
- [Databases](references/databases.md) <br>
- [Material Family Reference](references/materials.md) <br>
- [Scenario Methods](references/scenarios.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands, configuration snippets, and optional JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should cite the source database, version, system model, geography, reference unit, and entitlement status when reporting LCA values.] <br>

## Skill Version(s): <br>
1.7.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
