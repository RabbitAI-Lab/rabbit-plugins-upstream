## Description: <br>
Track and manage dependencies between OpenClaw skills. Scan skills for dependencies, visualize skill trees, detect circular dependencies, and manage skill versioning. Use when analyzing skill relationships, checking which skills depend on others, or managing skill installations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myrodar](https://clawhub.ai/user/myrodar) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill maintainers use this skill to inspect OpenClaw skill dependencies, detect missing or conflicting skills, visualize dependency trees, search the ClawHub registry, and install skills with dependency resolution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can persistently add multiple registry-sourced skills without a separate confirmation step. <br>
Mitigation: Before running skill-install.sh, manually review the full dependency set and publisher trust, then scan installed skills after installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/myrodar/skills/skill-deps) <br>
- [Publisher Profile](https://clawhub.ai/user/myrodar) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Terminal text with Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include dependency lists, dependency trees, conflict reports, search results, and install guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
