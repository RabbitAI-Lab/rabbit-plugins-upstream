## Description: <br>
Prepares Chinese drafts for publication by removing internal creation markers, generating title and summary options, preparing cover-image guidance, and writing local publication files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gogoingai](https://clawhub.ai/user/gogoingai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External authors, editors, and content teams use this skill to turn a finished Chinese Markdown draft into a publication-ready package with cleaned body text, candidate titles, a short description, optional cover-image metadata, and versioned local output files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create local publication directories and append changelog entries during normal use. <br>
Mitigation: Confirm the target draft and output paths before allowing writes, especially when the request is ambiguous. <br>
Risk: Automatic posting to external publishing platforms is not implemented in this release. <br>
Mitigation: Treat generated files as local publication assets and manually review them before any external publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gogoingai/skills/wenqu-publish) <br>
- [Project homepage](https://github.com/gogoingai/wenqu-skills/tree/master/wenqu-publish) <br>
- [Publication workflow](references/workflow.md) <br>
- [Title and summary writing guide](references/title-summary.md) <br>
- [Cover prompt guide](references/cover-prompt.md) <br>
- [Automatic publication extension notes](references/auto-publish.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown files and human-facing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes versioned local publication directories and appends a publication record when used in the documented workflow.] <br>

## Skill Version(s): <br>
0.1.15 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
