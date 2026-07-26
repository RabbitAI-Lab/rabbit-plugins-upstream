## Description: <br>
Open a browser tab so a human can highlight and comment on a Markdown file, then submit structured JSON comments the agent can use to revise the document. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxl-lxz](https://clawhub.ai/user/zxl-lxz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use comment-md to collect targeted human feedback on generated Markdown documents such as design docs, technical specs, READMEs, and PR descriptions. The agent reads the resulting structured comments, revises the source document, and summarizes how each comment was addressed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reviewed Markdown and comments may be exposed to third-party browser scripts loaded from jsDelivr. <br>
Mitigation: Avoid highly confidential documents unless dependencies are vendored or otherwise pinned and verified. <br>
Risk: The security verdict requires user review before installation. <br>
Mitigation: Review the submitted Markdown handling workflow and confirm the third-party script exposure is acceptable before deploying the skill. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/zxl-lxz/commentmd/tree/main/skills/commentmd) <br>
- [ClawHub skill page](https://clawhub.ai/zxl-lxz/skills/comment-md) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [Structured JSON comments with Markdown-oriented follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a comments JSON file next to the reviewed Markdown by default; static mode produces downloadable JSON.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
