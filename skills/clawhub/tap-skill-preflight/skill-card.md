## Description: <br>
Validate a SKILL.md before publishing by checking frontmatter completeness, semver versioning, and declared binary availability on PATH. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leonting1010](https://clawhub.ai/user/leonting1010) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill before ClawHub publication or when diagnosing missing requirements. It runs a local Python preflight check and returns a machine-readable result that identifies manifest or binary availability failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The checker reads the SKILL.md path supplied by the user. <br>
Mitigation: Run it only against skill folders or SKILL.md files you intend to inspect. <br>
Risk: An ok:true result can be overread as a full behavior or safety approval. <br>
Mitigation: Treat ok:true only as evidence that the manifest checks passed and declared binaries resolved on PATH. <br>
Risk: Binary availability checks depend on the local PATH where the command runs. <br>
Mitigation: Run the preflight in the same environment where the skill will be loaded or published. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leonting1010/skills/tap-skill-preflight) <br>
- [Publisher Profile](https://clawhub.ai/user/leonting1010) <br>


## Skill Output: <br>
**Output Type(s):** [json, shell commands, guidance] <br>
**Output Format:** [JSON validation result with concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The checker exits 0 on pass, 1 on validation failure, and 2 on usage or I/O error.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
