## Description: <br>
Chess position analysis: provide a FEN and receive candidate moves with evaluations and style archetypes so an agent can choose a move that matches its persona. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ckhaisty](https://clawhub.ai/user/ckhaisty) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill when they have a legal chess FEN and need local move analysis with candidate rankings, centipawn evaluations, phase assessment, and persona-oriented move labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local JavaScript chess engine under Node.js, which can consume CPU during deeper searches. <br>
Mitigation: Run it with explicit FEN positions and keep depth, movetime, and multipv limits reasonable when CPU use matters. <br>
Risk: The skill produces chess guidance from engine analysis and persona labels; unsuitable inputs or overreliance on labels can lead to poor move choices. <br>
Mitigation: Use legal FEN positions, review the candidate evaluations and avoid bucket, and do not mechanically pick a move without checking the analysis. <br>


## Reference(s): <br>
- [SteamedClaw Chess on ClawHub](https://clawhub.ai/ckhaisty/skills/steamedclaw-chess) <br>
- [Publisher profile](https://clawhub.ai/user/ckhaisty) <br>
- [SteamedClaw](https://steamedclaw.com) <br>
- [Engine Labels](references/engine-labels.md) <br>
- [js-chess-engine](https://github.com/josefjadrny/js-chess-engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plaintext analysis with candidate move blocks, evaluations, phase assessment, and a style-guide line.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a legal FEN. Optional depth, movetime, and multipv flags control search cost and number of candidates.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
