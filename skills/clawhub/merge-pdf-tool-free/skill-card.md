## Description: <br>
PDF合并工具（免费版） helps an agent merge multiple PDF files into one document, with support for page ordering, page-range selection, bookmark generation, and batch processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to direct an agent through local PDF merge tasks, including combining selected files, choosing page ranges, adding bookmarks, and saving the merged output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can involve reading source PDFs and writing output files, which may expose sensitive document contents to the agent runtime. <br>
Mitigation: Use exact source paths and avoid sensitive PDFs unless the user is comfortable with the agent reading and writing those files. <br>
Risk: A merge operation can overwrite an existing PDF if the output path already exists. <br>
Mitigation: Confirm the output path before writing and ask before replacing existing PDF files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/merge-pdf-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with code examples, shell commands, configuration snippets, and generated PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read source PDFs and write merged PDF outputs on the local filesystem.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
