## Description:

This skill helps turn website URLs, landing pages, or links into promotional, social-ad, or product-demo videos by capturing the site, deriving brand context, storyboarding, voiceover planning, building, and validating with a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and content teams use this skill to ask an agent to create website-based promotional, social-ad, or product-demo video work through the dLazy CLI service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website or link context, and explicitly attached files are sent to dLazy's hosted service.

Mitigation: Use the skill only when external dLazy processing is intended, and avoid attaching private or sensitive files unless that upload is approved.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Use an appropriate organization-scoped key, rotate or revoke it from the dLazy dashboard when needed, or provide it per run with the DLAZY_API_KEY environment variable to avoid persistent local storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of a dLazy SaaS CLI flow and may involve external API calls and upload of explicitly attached local files when the user runs the CLI.]

## Skill Version(s):

1.3.7 (source: ClawHub release evidence; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
