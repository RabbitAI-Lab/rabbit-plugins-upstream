## Description: <br>
Builds a Gauntlet knowledge base from AST extraction and AI enrichment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to initialize or refresh codebase knowledge for Gauntlet challenges by extracting structure, enriching entries, and saving a local .gauntlet/knowledge.json file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill indexes the target repository and writes local codebase knowledge, which could include unrelated private files if pointed at the wrong directory. <br>
Mitigation: Run it only against intended codebases and avoid directories that contain unrelated private files or secrets. <br>
Risk: The generated knowledge base may contain incomplete or inaccurate AI-enriched explanations. <br>
Mitigation: Review .gauntlet/knowledge.json and coverage gaps before relying on the extracted knowledge for challenge work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-extract) <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and a local JSON knowledge-base file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or refreshes .gauntlet/knowledge.json and reports category coverage, gaps, and difficulty distribution.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
