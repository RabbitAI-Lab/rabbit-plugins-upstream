## Description: <br>
Trigger a one-shot workflow that clones or pulls a Git repository, generates a structured wiki from it using the CodeWiki CLI, and can optionally render the result into static MkDocs or VitePress sites with an HTTP preview. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangsier-xyz](https://clawhub.ai/user/jiangsier-xyz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical teams use this skill to generate repository documentation wikis from GitHub, SSH, HTTPS, or local repository inputs. It also supports optional static-site rendering and local preview when users need a browsable documentation site. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can clone or pull repositories and process local folders, which may expose sensitive source content to the CodeWiki workflow if the user selects the wrong input. <br>
Mitigation: Require explicit user confirmation before execution and avoid pointing the skill at sensitive local folders unless those contents are intended for documentation generation. <br>
Risk: Optional rendering can download Python or Node rendering dependencies and create local build artifacts. <br>
Mitigation: Skip rendering when runtime package installation is not acceptable, and review the generated local wiki and site outputs before publishing or sharing them. <br>


## Reference(s): <br>
- [CodeWiki](https://github.com/FSoft-AI4Code/CodeWiki) <br>
- [ClawHub Skill Page](https://clawhub.ai/jiangsier-xyz/skills/codewiki) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown documentation files, optional static site files, and concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local repository clones, wiki directories, MkDocs or VitePress site outputs, and optional localhost preview URLs.] <br>

## Skill Version(s): <br>
1.2.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
