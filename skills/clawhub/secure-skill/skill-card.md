## Description: <br>
Scans skill directories for code, prompt, and supply chain security issues, produces Markdown or JSON reports, and can install skills from a local registry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garsonjw](https://clawhub.ai/user/garsonjw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit local skill directories for static code, prompt, and supply chain risks, then summarize findings for review. Teams can also use its installer workflow to copy selected skills from a trusted local registry into a project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner has an automatic install side effect and can modify .claude/skills while running a scan. <br>
Mitigation: Run it only in a disposable or backed-up workspace until installation is gated behind explicit consent. <br>
Risk: The installer can replace an existing destination skill directory before copying from the local registry. <br>
Mitigation: Use only trusted registry entries and confirm the target project root and skill names before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/garsonjw/skills/secure-skill) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/garsonjw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown table report or JSON scan results, with command-line usage and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline file-system scan; strict mode can treat HIGH findings as failures.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
