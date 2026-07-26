## Description: <br>
Deep security analysis of an individual skill before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itsnishi](https://clawhub.ai/user/itsnishi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to inspect an individual agent skill before installation or marketplace review. It produces severity-ranked findings and recommendations for frontmatter, hidden instructions, shell patterns, supporting files, obfuscation, and supply-chain signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Package verification may contact PyPI or npm with package names found during a scan. <br>
Mitigation: Run it only on skill directories intended for analysis, and avoid scanning private projects if exposing internal package names to public registries is unacceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itsnishi/skills/scan-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-style security report with severity-ranked findings and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include frontmatter analysis, supporting file inventory, and PyPI/npm package verification results.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
