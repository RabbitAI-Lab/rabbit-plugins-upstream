## Description:

Turns user-provided presentations, documents, spreadsheets, and PDFs into narrated explainer, reporting, courseware, or training videos through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating explainer, report, courseware, or training videos can provide documents and work with a project-based dLazy assistant to develop the video across multiple turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached documents are sent to a third-party hosted service.

Mitigation: Avoid confidential documents unless dLazy's terms and your organization's policy allow their use.

Risk: Authentication can store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: The skill installs or invokes a third-party CLI package without server-resolved GitHub import provenance.

Mitigation: Review the pinned npm package and linked source before installing if supply-chain provenance matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI repository (linked in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Video links]

**Output Format:** [Chat text with links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations; generated media is hosted by dLazy.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
