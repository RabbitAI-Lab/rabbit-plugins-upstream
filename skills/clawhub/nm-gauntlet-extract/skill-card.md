## Description: <br>
Builds the gauntlet knowledge base from AST extraction and AI enrichment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to build or refresh a local `.gauntlet/knowledge.json` knowledge base for a codebase, combining AST extraction with AI-enriched explanations and cross-references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes or updates `.gauntlet/knowledge.json` in the target repository. <br>
Mitigation: Review changes to `.gauntlet/knowledge.json` before committing or using them as codebase knowledge. <br>
Risk: The artifact invokes an external gauntlet extractor script from the plugin environment. <br>
Mitigation: Verify the extractor script before use in environments where plugin code is treated as sensitive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-extract) <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and a generated JSON knowledge file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes `.gauntlet/knowledge.json` and reports category summaries, coverage gaps, and difficulty distribution.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
