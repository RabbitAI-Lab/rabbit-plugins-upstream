## Description: <br>
semantic-split helps agents turn natural-language task requests into structured requirement blocks, execution steps, work packages, and reusable JSON task templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to decompose task requests, extract 5W2H and constraint signals, plan execution steps, and save reusable JSON task templates for later matching. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad planning requests. <br>
Mitigation: Prefer explicit invocation and require confirmation before using generated plans or saving reusable templates. <br>
Risk: The skill can persist reusable task templates to local JSON storage. <br>
Mitigation: Review generated JSON before reuse and restrict writes to the configured standardization data directory. <br>
Risk: The skill may install dependencies or download ML models during setup or semantic matching. <br>
Mitigation: Approve dependency installation and model downloads before running setup or model-loading commands. <br>
Risk: Optional automation may process memory logs when configured. <br>
Mitigation: Avoid sensitive tasks, disable automation unless needed, or scrub memory sources before automated template generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/semantic-split) <br>
- [JSON structure specification](references/json_schema.md) <br>
- [Progressive loading decision tree](references/loading_decision_tree.md) <br>
- [Planning rules](references/planning_rules.md) <br>
- [Permissions and risk notes](references/permissions.md) <br>
- [Attribution](references/attribution.md) <br>
- [FlagEmbedding project](https://github.com/FlagOpen/FlagEmbedding) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [JSON and Markdown guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes one plain-text task request up to about 2000 characters; may persist reusable JSON templates under the configured standardization data directory.] <br>

## Skill Version(s): <br>
3.1.1 (source: evidence release metadata, artifact frontmatter, artifact _meta.json, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
