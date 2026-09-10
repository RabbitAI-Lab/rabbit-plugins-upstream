## Description:

Adversarial, code-cited audit of ML research claims, objectives, leakage, controls, and baseline fairness with ranked risks and explicit falsification tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers, ML researchers, reviewers, and technical evaluators use this skill to challenge experimental claims by tracing implementation evidence, ranking validity risks, and proposing falsification checks without treating static review as reproduced results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to inspect research repositories and propose experiments, which could be mistaken for executed or reproduced evidence.

Mitigation: Require the output to separate static inference from executed evidence and to label proposed scripts, commands, paid compute, data downloads, tracker writes, or repository changes as requiring separate authorization.

Risk: Skill instructions are not a sandbox and cannot override host permissions or user scope.

Mitigation: Install and run the skill only in a host with appropriate permission controls, and keep sensitive source excerpts, secrets, private records, tracker exports, and exploit-ready details out of public outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/antreasantoniou/skills/ml-research-skeptical-audit)
- [Publisher Profile](https://clawhub.ai/user/antreasantoniou)
- [Source Repository](https://github.com/AntreasAntoniou/ml-research-skeptical-audit.git)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown with code citations, ranked findings, risk notes, and falsification proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguishes reviewed, executed, reproduced, and unchecked evidence; proposed commands or experiments must be labeled as not run unless separately authorized.]

## Skill Version(s):

1.0.0 (source: changelog, released 2026-09-05)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
