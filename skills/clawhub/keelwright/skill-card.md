## Description: <br>
Keelwright helps agents run safer autonomous coding loops by combining security gates, autonomy controls, self-healing workflow checks, and plain-language reports for users who cannot review every line of AI-generated code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ratingtesting](https://clawhub.ai/user/ratingtesting) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and non-developer builders load Keelwright before coding sessions to have an agent propose and enforce security, quality, loop-control, and evidence-checking safeguards while producing plain-language status and review guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to make persistent project changes and maintain cross-session state. <br>
Mitigation: Require approval for first-load bootstrap writes, deleted-file recreation, and any changes to tracking files unless the project owner has explicitly opted into them. <br>
Risk: Autonomous coding workflows can reach high-impact actions such as package installation, commits, pushes, rollbacks, or deployments. <br>
Mitigation: Use checkpoint-style approval for package installation, git commit or push, auth, payment, data deletion, production rollback, and deploy actions. <br>
Risk: Claims about gate effectiveness or QA outcomes can be misleading if they rely on self-report instead of artifacts. <br>
Mitigation: Require on-disk evidence, run the relevant tests or scanners, and validate QA claims with the included integrity checks before treating results as proven. <br>


## Reference(s): <br>
- [Keelwright README](README.md) <br>
- [Security Gates](references/security-gates.md) <br>
- [Phases](references/phases.md) <br>
- [Circuit Breaker](references/circuit-breaker.md) <br>
- [QA Testing](references/qa-testing.md) <br>
- [QA Results](qa-results/README.md) <br>
- [Provenance, Credits, and License Table](references/provenance.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline code and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project tracking files and verification artifacts when its workflows are followed.] <br>

## Skill Version(s): <br>
1.5.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
