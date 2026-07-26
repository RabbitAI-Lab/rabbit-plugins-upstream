## Description: <br>
Automatically analyzes a source file or project directory and generates 4+1 architecture view Markdown files with Mermaid diagrams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[langlitaosha80](https://clawhub.ai/user/langlitaosha80) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to inspect codebases and produce architecture documentation across logical, process, physical, development, and scenario views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or changes arcview files and manages backups in the target project. <br>
Mitigation: Run it in a clean working tree or disposable copy, inspect generated Markdown before committing, and confirm the target path before allowing writes. <br>
Risk: The skill may keep a hidden cache of architecture data derived from the repository. <br>
Mitigation: Avoid using it on sensitive private repositories unless the cache location and contents are acceptable, and remove the cache after use when needed. <br>
Risk: Generated Mermaid content may be sent to third-party Mermaid validation services. <br>
Mitigation: Run with network access disabled or confirm that remote validation is explicitly intended before analyzing confidential code. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/langlitaosha80/skills/arc4plus1) <br>
- [Mermaid Live](https://mermaid.live) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown files with Mermaid diagram code blocks and a README] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates an arcview directory in the target project and may maintain backups or a hidden architecture cache.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence; artifact frontmatter and package.json list 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
