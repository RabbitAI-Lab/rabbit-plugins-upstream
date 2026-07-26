## Description: <br>
Creates source-level 80k+ word project CookBooks as LaTeX, PDF, and EPUB for websites, documentation, repositories, and other project materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[samonysh](https://clawhub.ai/user/samonysh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, architects, and technical writers use this skill to turn project documentation, source code, APIs, papers, or repository materials into a deep technical cookbook. It guides agents toward LaTeX-first book projects with PDF and EPUB outputs, diagrams, source-level analysis, references, word counts, and validation reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to read project documentation, source paths, or other materials supplied by the user. <br>
Mitigation: Use it only with materials intended for cookbook generation and review the selected input paths before execution. <br>
Risk: Remote fetching, dependency installation, image downloads, and unsafe LaTeX options can introduce side effects if approved without review. <br>
Mitigation: Keep the default offline and fail-closed posture; approve network access, installs, downloads, or shell escape only when the source and environment are trusted. <br>
Risk: Long generated technical books may contain incorrect or unsupported project claims if sources are incomplete. <br>
Mitigation: Review generated references, source citations, validation reports, and word-count metadata before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/samonysh/skills/project-cookbook-latex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with LaTeX, shell, configuration, and project-structure examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides generation of LaTeX projects, PDFs, EPUBs, diagrams, references, word-count metadata, and validation reports; remote access, installs, and LaTeX shell escape require explicit approval.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
