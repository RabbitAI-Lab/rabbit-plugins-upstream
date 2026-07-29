## Description: <br>
Ppshu Github helps agents create self-contained HTML diagrams, charts, and interactive prototypes, save them into a project-local .ppshu gallery, and present them to users. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ppshux](https://clawhub.ai/user/ppshux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, designers, and knowledge workers use this skill to turn explanations into visual diagrams, architecture sketches, charts, state flows, or clickable UI prototypes that can be opened offline and reviewed from a generated gallery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates local HTML files and an index under the active project's .ppshu directory, which may add files to sensitive or shared repositories. <br>
Mitigation: Review generated files before sharing, add .ppshu to .gitignore when appropriate, or set PPSHU_DIR or --dir to an approved output location. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ppshux/skills/ppshu) <br>
- [README](artifact/README.md) <br>
- [ppshu HTML drawing guide](artifact/references/html_cookbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell commands and self-contained HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated HTML is saved under .ppshu/ by default, with sequential filenames and an index.html gallery; PPSHU_DIR or --dir can redirect the output directory.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and manifest.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
