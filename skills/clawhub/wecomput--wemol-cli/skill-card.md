## Description:

Helps agents find WeMol scientific documentation and workflows, run supported analyses, and retrieve results through the WeMol CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wecomput](https://clawhub.ai/user/wecomput)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other WeMol users can look up scientific methods, discover suitable workflows, submit analyses, check jobs, and retrieve results using their selected WeMol account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation may prompt external scientific lookup or local CLI installation without a narrowly stated request.

Mitigation: Keep host command approvals enabled and require explicit confirmation before installing the CLI.

Risk: Job submissions may upload scientific inputs and use paid or quota-backed resources.

Mitigation: Confirm the intended channel and account, inputs, and cost or quota before submission.

Risk: Downloading artifacts writes local files; canceling jobs changes account-backed work.

Mitigation: Require explicit confirmation before downloads or cancellations and verify the selected job and channel.

## Reference(s):

- [WeMol CLI on ClawHub](https://clawhub.ai/wecomput/skills/wemol-cli)
- [WeMol CLI project homepage (listed in skill metadata)](https://github.com/wecomput/wemol-cli)
- [WeMol platform](https://wemol.wecomput.com)
- [Task guide index](guides/index.md)
- [CLI setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown explanations, workflow guidance, and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report job status and retrieved artifact locations.]

## Skill Version(s):

1.2.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
