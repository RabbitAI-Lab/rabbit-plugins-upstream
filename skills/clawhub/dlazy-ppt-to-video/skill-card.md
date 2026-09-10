## Description:

Converts PPT, PowerPoint, Keynote, and related document inputs into explainer, pitch, courseware, or training videos through dLazy's hosted file-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and business users use this skill to turn presentation files into video projects with dLazy. It helps an agent start or continue a hosted file-to-video workflow, attach source files, and guide follow-up turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the dLazy CLI globally adds a persistent executable from the npm supply chain.

Mitigation: Review the dLazy CLI source before installing, or use the pinned npx invocation when a global binary is not needed.

Risk: Attached local files are uploaded to dLazy media storage for hosted processing.

Mitigation: Only attach files that are appropriate to upload to dLazy and comply with the user's data handling requirements.

Risk: The dLazy API key can authorize work in the user's organization if exposed.

Mitigation: Store the key with local user permissions and rotate or revoke it if the machine or npm supply chain is suspected to be compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt-to-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; the hosted dLazy workflow may create video project outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy authentication and may upload attached local files to dLazy-hosted endpoints.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
