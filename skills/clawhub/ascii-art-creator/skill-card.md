## Description: <br>
Generate banners, boxes, cowsay-style art, tables, and image-to-ASCII with multiple fonts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, CLI authors, and documentation writers use this skill to generate terminal-friendly banners, boxed notes, tables, cowsay-style messages, and image-to-ASCII output for scripts, logs, and READMEs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional CI verification helper can execute discovered Python self-tests or test files when run against a repository or skill folder. <br>
Mitigation: Run ci/verify_product.py only on trusted folders, or inside a sandbox without secrets or sensitive network access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/ascii-art-creator) <br>
- [Artifact README](artifact/README.md) <br>
- [ASCII Art CLI source](artifact/ascii_art.py) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text and Markdown with inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Terminal-oriented ASCII output; image conversion supports Pillow, PyMuPDF, or PPM/PGM/PBM inputs when available.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata; artifact frontmatter states 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
