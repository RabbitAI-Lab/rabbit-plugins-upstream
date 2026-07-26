## Description: <br>
Read Figma design context from Multica issue figma_urls without Figma MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xianyu-cursor](https://clawhub.ai/user/xianyu-cursor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and repair agents use this skill to collect Figma design context for UI repair work, including summaries, node metadata, screenshots, style details, Code Connect clues, and artifact paths that should be reviewed before changing code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Figma credentials and calls Figma APIs. <br>
Mitigation: Use it only in trusted workspaces, keep credentials out of logs and commits, and review generated artifacts for redaction before sharing. <br>
Risk: Generated design artifacts and temporary issue files may contain project-specific UI context. <br>
Mitigation: Keep .multica/figma-context and .multica/tmp out of commits and review any local Git exclude changes. <br>
Risk: Figma URLs alone can be ambiguous and may point to broad or nested nodes. <br>
Mitigation: Read the generated summary, manifest, design properties, Code Connect output, and screenshots before relying on the design context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xianyu-cursor/skills/templates) <br>
- [Repair Expert Usage](references/repair-expert-usage.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [Node Expansion Rules](references/node-expansion-rules.md) <br>
- [Code Connect Rules](references/code-connect-rules.md) <br>
- [Style Extraction Checklist](references/style-extraction-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries, JSON artifacts, CSS hints, screenshots, and CLI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated artifacts are written under .multica/figma-context and should not be committed.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
