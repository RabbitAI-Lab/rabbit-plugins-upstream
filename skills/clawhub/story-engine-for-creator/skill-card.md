## Description: <br>
Story Causal Engine audits and generates narrative outlines by checking causal chains, plot logic, character consistency, world rules, and timeline alignment. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, writers, narrative designers, and developers use this skill to convert natural-language outlines into causal story chains, audit plot, character, world-building, and timeline consistency, and generate draft narrative text or repair suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private story drafts, plot details, and character context may be sent to an attached cloud LLM provider. <br>
Mitigation: Use local/default operation for private manuscripts, or attach a cloud provider only after accepting that provider's handling of story context. <br>
Risk: Generating a novel writes audit_report.html in the working directory and may overwrite an existing file with that name. <br>
Mitigation: Run generation in a workspace where that filename is disposable, or move or rename any existing audit_report.html first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/story-engine-for-creator) <br>
- [Project homepage](https://github.com/NOHN-AI/story-engine) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Python objects, generated narrative text, Markdown story drafts, and an HTML audit report file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write audit_report.html in the working directory when generating a novel.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
