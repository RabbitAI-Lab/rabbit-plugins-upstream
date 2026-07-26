## Description: <br>
Generate Excalidraw diagrams (flowcharts, sequences, architecture) as valid .excalidraw JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, technical writers, and agents use this skill to create flowchart, sequence, and architecture diagrams as version-controllable Excalidraw JSON files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running bundled verification scripts on untrusted repositories or in environments with secrets can expose files outside the intended diagram workflow. <br>
Mitigation: Use the main excalidraw_cli.py for local diagram generation and run ci/verify_product.py only on trusted folders in environments without sensitive secrets. <br>
Risk: Installing from an unpinned main-branch curl command can fetch code different from the reviewed release artifact. <br>
Mitigation: Install from a pinned release or this reviewed artifact instead of an unpinned GitHub main-branch URL. <br>
Risk: Merge, info, and export commands read and write local diagram files selected by the user. <br>
Mitigation: Read and write only diagram files you intend to process and review output paths before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/excalidraw-cli) <br>
- [Publisher profile](https://clawhub.ai/user/itspremkumar) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and generated Excalidraw JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI can generate .excalidraw JSON, merge Excalidraw files, summarize diagram metadata, and export SVG or PNG when optional image dependencies are available.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
