## Description: <br>
Solve Boggle boards by finding valid German and English words on a 4x4 letter grid using dictionary-backed search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christianhaberl](https://clawhub.ai/user/christianhaberl) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to solve Boggle boards from a confirmed 4x4 grid, with English and German results returned as separate word lists and scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads large dictionary files from GitHub on first use and caches them locally. <br>
Mitigation: Review or preinstall the dictionary files for offline or high-integrity environments, and verify their source before running the solver. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/christianhaberl/skills/boggle) <br>
- [OpenClaw repository](https://github.com/openclaw/openclaw) <br>
- [Dictionary data source](https://github.com/christianhaberl/boggle-openclaw-skill/tree/main/data) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with command examples; solver output is plain text or JSON when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns word lists grouped by length, Boggle scores, total word count, total score, and solve time.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
