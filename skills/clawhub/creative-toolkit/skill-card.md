## Description:

Helps agents compose MeiGen image and video generation, dedicated image tools, and optional creative planning within an existing workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jau123](https://clawhub.ai/user/jau123)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to guide an agent through MeiGen image and video creation, image editing, and optional creative planning while preserving their requested scope and budget.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, images, videos, and reference material are sent to MeiGen cloud services; uploaded references may have shareable URLs.

Mitigation: Send only content approved for cloud processing and treat uploaded reference links as shareable, not private.

Risk: Generation can consume purchased credits.

Mitigation: Check current prices and stay within the user's approved count and budget before submitting paid jobs.

Risk: Granting library and history permissions exposes saved content and past prompts to the connected agent.

Mitigation: Grant these OAuth permissions only when the user wants the agent to use saved content or prior prompts.

## Reference(s):

- [MeiGen ClawHub skill](https://clawhub.ai/jau123/skills/creative-toolkit)
- [MeiGen OpenClaw setup](https://www.meigen.ai/mcp?tab=openclaw)
- [Providers and configuration](references/providers.md)
- [Troubleshooting and data handling](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Text]

**Output Format:** [Markdown or text with generation links and task status when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated-media URLs or saved paths; cloud generation requires authorization and credits.]

## Skill Version(s):

3.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
