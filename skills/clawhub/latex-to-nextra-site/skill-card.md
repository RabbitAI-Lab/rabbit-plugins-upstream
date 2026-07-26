## Description: <br>
Converts project-cookbook-latex LaTeX projects into Chinese Nextra documentation sites that preserve diagrams, code blocks, formulas, and tables, with outputs ready for GitHub, Vercel, or Docker deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to convert structured LaTeX cookbook, ebook, or paper projects into multilingual Nextra documentation sites. It guides preservation of PlantUML, Draw.io, Mermaid, code, math, tables, downloads, and deployment assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent to run networked or state-changing npm, Docker, git, GitHub, and Vercel workflows. <br>
Mitigation: Require explicit user approval before each networked or state-changing command, and keep conversion work offline by default. <br>
Risk: Untrusted LaTeX projects or diagram filenames may be unsafe when processed by shell-based workflows. <br>
Mitigation: Avoid untrusted LaTeX repositories, keep LaTeX shell escape disabled unless the user consents in a sandboxed trusted environment, inspect diagram filenames for shell metacharacters, and quote paths in shell commands. <br>
Risk: A copied .npmrc may expose private registry credentials during commit, build, or deployment. <br>
Mitigation: Review any .npmrc before use, remove private registry tokens, and avoid committing secret-bearing configuration files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samonysh/skills/latex-to-nextra-site) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/samonysh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code blocks, and project file specifications] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides generation of a Nextra/Next.js project directory with GitHub, Vercel, Docker, diagram-rendering, and validation assets.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
