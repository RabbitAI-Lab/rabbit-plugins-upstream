## Description: <br>
Open a browser tab so a human can highlight and comment on a Markdown file, then return structured comments the agent can read and address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxl-lxz](https://clawhub.ai/user/zxl-lxz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and writing agents use this skill to collect targeted human feedback on generated Markdown documents such as design docs, technical specs, READMEs, and PR descriptions before revising them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The review flow opens Markdown through a local browser-based process and writes a comments JSON file beside the source document. <br>
Mitigation: Use it only on documents appropriate for local browser review, and avoid documents containing secrets or regulated data unless the local server behavior has been verified. <br>
Risk: Human comments may become stale if the Markdown file changes during review. <br>
Mitigation: Check the reported change indicator and warn the user before applying comments to a modified source document. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/zxl-lxz/commentmd/tree/main/skills/commentmd) <br>
- [ClawHub skill page](https://clawhub.ai/zxl-lxz/skills/commentmd) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions with shell commands and JSON comment data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or consumes a comments JSON file for the reviewed Markdown document.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
