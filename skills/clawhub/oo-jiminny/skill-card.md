## Description: <br>
Jiminny lets agents search and retrieve data from a user's OOMOL-connected Jiminny account through the oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external agents use this skill to retrieve Jiminny activities, summaries, transcripts, action items, scorecards, organization details, and related account records through an authenticated OOMOL connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Jiminny transcripts, comments, coaching feedback, scorecards, and user lists may contain sensitive business data. <br>
Mitigation: Retrieve only the records needed for the user's task and handle returned Jiminny data as confidential account data. <br>
Risk: Future versions could add write or destructive actions that change or remove Jiminny data. <br>
Mitigation: Review future releases carefully and require explicit user confirmation before running any action tagged write or destructive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jiminny) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Jiminny homepage](https://jiminny.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses return Jiminny account data under data and an execution id under meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
