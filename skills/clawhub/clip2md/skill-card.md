## Description: <br>
Clip2MD lets an agent configure a clip2md token, submit web page URLs for Markdown clipping, check quota, query task status, and wait for completion or failure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kllb520](https://clawhub.ai/user/kllb520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when they want an agent to save web pages as Markdown clipping tasks and report quota, task status, errors, and readiness without exposing the user's token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a clip2md access token locally without restrictive permissions. <br>
Mitigation: Check permissions on ~/.clip2md/config.json, avoid using the skill on shared machines, and rotate or remove the token when it is no longer needed. <br>
Risk: Broad invocation terms can cause selected URLs to be submitted to clip2.md unintentionally. <br>
Mitigation: Confirm the target URL and user intent before running clip commands, especially for generic requests to clip or save a page. <br>


## Reference(s): <br>
- [Clip2MD ClawHub Skill Page](https://clawhub.ai/kllb520/skills/clip2md) <br>
- [clip2md API endpoint](https://clip2.md/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Plain text CLI summaries with optional Markdown clipping content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; stores a clip2md token in ~/.clip2md/config.json and submits selected URLs to clip2.md.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
