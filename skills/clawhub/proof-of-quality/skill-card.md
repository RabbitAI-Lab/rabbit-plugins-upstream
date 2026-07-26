## Description: <br>
Proof-of-Quality runs a local Node.js proof-of-work check that reads a skill file, computes a simple benchmark score, and emits a hash, nonce, and score when the threshold is met. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[kunoiiv](https://clawhub.ai/user/kunoiiv) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill maintainers can use this as a local demonstration of proof-of-work scoring for skills, producing a shareable PoQ result. The security evidence warns not to rely on the result for real approval or verification decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PoQ result could be mistaken for a trustworthy approval, security, or quality signal. <br>
Mitigation: Treat outputs as demonstration-only and make real verification decisions using independent review, tests, and security scans. <br>
Risk: The script reads a local skill path and the artifact suggests recurring cron execution. <br>
Mitigation: Run it only on explicit intended paths and avoid scheduled execution unless recurring local reads and hashing are deliberate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kunoiiv/skills/proof-of-quality) <br>
- [Publisher profile](https://clawhub.ai/user/kunoiiv) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped proof output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Console output includes a benchmark score, hash, and nonce; artifact guidance describes a shareable PoQ JSON object.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
