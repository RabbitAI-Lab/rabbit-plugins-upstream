## Description:

Helps turn PPT, Word, Excel, and PDF documents into narrated explainer, reporting, courseware, or training videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn supplied documents into narrated explainer, report, courseware, or training videos through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached files are uploaded to dLazy's hosted service.

Mitigation: Attach only files you intend to share with dLazy.

Risk: The external CLI uses a locally stored dLazy API key.

Mitigation: Protect the key and rotate or revoke it from the dLazy dashboard if needed.

Risk: The workflow requires installing or running dLazy's external npm CLI.

Mitigation: Review the CLI before use; use npx instead of a global install to reduce local persistence.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-file-to-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video links, Guidance]

**Output Format:** [Text with links to generated video results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document-to-video tasks may continue across project sessions.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
