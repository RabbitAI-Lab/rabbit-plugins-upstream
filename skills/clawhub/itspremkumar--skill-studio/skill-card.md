## Description: <br>
Local-first studio to author, test, version & publish agent skills with a real backend, auth, test-runner UI, and one-click ClawHub publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use ClawHub Studio to create, test, version, and publish agent skills from a local web interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local API can mint session tokens without credentials. <br>
Mitigation: Run the studio only on a trusted single-user machine and keep the localhost port private. <br>
Risk: Self-tests execute skill code with the user's local permissions. <br>
Mitigation: Review skill contents before testing and run self-tests only for skills from trusted or inspected sources. <br>
Risk: Publishing can use an already authenticated ClawHub CLI session. <br>
Mitigation: Use dry-run publishing by default and switch to live publishing only after verifying the target account and release contents. <br>


## Reference(s): <br>
- [ClawHub Studio release page](https://clawhub.ai/itspremkumar/skills/skill-studio) <br>
- [README](README.md) <br>
- [Architecture](ARCHITECTURE.md) <br>
- [API](API.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON responses, code files, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs local self-tests and dry-run publishing workflows before release.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
