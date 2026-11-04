## Description:

ppt to video, word to video, excel to video, pdf to video, document to video — parse, outline, storyboard, voiceover, build, validate. Use when the user gives a document and wants an explainer, report broadcast, courseware, or training video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People who need to communicate information from a PPT, Word, Excel, or PDF use this skill to create an explainer, report, courseware, or training video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documents and prompts are sent to dLazy's hosted service, and the external CLI distribution and backend were not fully audited.

Mitigation: Upload only documents you are permitted to share, confirm the intended project, and review the service's costs and retention terms.

Risk: Sharing an API key in chat can expose access to the user's dLazy organization.

Mitigation: Use the device login flow or provide the key through an environment variable instead of sharing it in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy homepage](https://dlazy.com)
- [CLI source listed in the skill documentation](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, Text, Guidance]

**Output Format:** [Generated video with text responses in the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result depends on the uploaded document and selected project.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
