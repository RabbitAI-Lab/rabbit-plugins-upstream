## Description: <br>
Opens a browser-based Markdown review view so a human can highlight text, add comments, and return structured feedback JSON for the agent to process. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxl-lxz](https://clawhub.ai/user/zxl-lxz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill after drafting Markdown documents such as design docs, technical specs, READMEs, or PR descriptions to collect targeted human review comments before revising the document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Markdown review page loads third-party CDN JavaScript, which could expose private Markdown content during review. <br>
Mitigation: Use the skill only with non-sensitive Markdown unless the external scripts are vendored locally or protected with pinned integrity checks and a restrictive content security policy. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxl-lxz/skills/md-comment) <br>
- [Source repository path](https://github.com/zxl-lxz/commentmd/tree/main/skills/commentmd) <br>
- [Publisher profile](https://clawhub.ai/user/zxl-lxz) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance] <br>
**Output Format:** [Structured JSON comments with quoted Markdown excerpts, anchor context, timestamps, and a changed-file indicator.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The default output is a comments JSON file next to the reviewed Markdown file; static review mode downloads the same JSON for the agent to import.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
