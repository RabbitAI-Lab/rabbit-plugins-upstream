## Description: <br>
Academic paper reading and literature research skill for paper-reading, literature review, arXiv, DOI, PDF, paper title, or paper list tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pengheliu](https://clawhub.ai/user/pengheliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, reviewers, and engineers use this skill to triage academic papers, apply a Li Mu inspired three-pass reading workflow, critique methods and experiments, compare papers, plan reproductions, and build literature maps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML notes may contain sensitive paper content and load MathJax or Mermaid from a public CDN when viewed. <br>
Mitigation: For sensitive papers, avoid opening generated HTML online or adapt the note to use local/offline assets. <br>
Risk: The skill may install pymupdf, write files under ~/paper-notes, start a localhost preview server, and open a browser. <br>
Mitigation: Review the proposed commands, output path, and local server behavior before execution in the target environment. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/PengheLiu/mli-paper-reading-skill/tree/main/skills/mli-paper-reading) <br>
- [ClawHub skill page](https://clawhub.ai/pengheliu/skills/mli-paper-reading) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated local HTML reading notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write HTML notes under ~/paper-notes, start a localhost preview server, open a browser, and load MathJax or Mermaid from a public CDN when the note is viewed.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
