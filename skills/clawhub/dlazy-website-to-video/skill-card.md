## Description:

Turns a website URL into a promotional video, social ad, or product demo using the dLazy hosted website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a website or landing page into a promotional video, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to the dLazy hosted service.

Mitigation: Use the service only if sharing this content with dLazy is acceptable.

Risk: Attached local files are uploaded to dLazy media storage.

Mitigation: Review attachments before sending and omit sensitive files.

Risk: Login stores a dLazy API key locally, and a global CLI installation persists.

Mitigation: Protect or rotate the key as needed; use the on-demand npx option if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source (linked in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Streaming text responses from the hosted video workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports project-scoped follow-up; video creation runs through the dLazy hosted service.]

## Skill Version(s):

1.3.26 (source: ClawHub release evidence; skill frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
