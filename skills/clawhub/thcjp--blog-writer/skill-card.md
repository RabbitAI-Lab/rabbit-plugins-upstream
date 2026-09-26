## Description: <br>
Blog Writer helps agents draft blog posts from topics and research material by matching an author's writing style, then supports review, notes-platform publishing, and example-library maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, independent developers, and teams use this skill to turn topics and research notes into opinionated, conversational blog drafts in a calibrated author style. It also supports draft iteration, publishing to a configured notes database, and archiving finalized examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Drafts may contain private, customer, business, or proprietary material and the skill directs draft publication to an external notes database. <br>
Mitigation: Review draft sensitivity before use and publish only when the destination, access controls, and content handling are approved. <br>
Risk: The skill declares broad command execution and file-writing capabilities without clear limits. <br>
Mitigation: Run the skill in a sandbox, require explicit confirmation before exec, publish, or save actions, and remove exec access if it is not needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/blog-writer) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown blog drafts with configuration notes and publishing or file-maintenance guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default draft length is 800-1500 characters unless the user specifies otherwise.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
