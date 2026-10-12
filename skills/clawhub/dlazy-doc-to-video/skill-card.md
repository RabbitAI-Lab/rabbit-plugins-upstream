## Description:

Helps turn documents into narrated explainer, report, courseware, or training videos through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn documents into narrated explainers, report summaries, courseware, and training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to the third-party dLazy service.

Mitigation: Review the service terms and only upload documents you are comfortable sharing with dLazy.

Risk: The saved API key grants access to the user's dLazy account.

Mitigation: Treat ~/.dlazy/config.json as sensitive and rotate the key from the dLazy dashboard if needed.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text or Markdown with video-generation results and project guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document-to-video work runs through the dLazy service.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata; skill frontmatter says 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
