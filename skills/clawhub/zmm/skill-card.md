## Description:

詹明明 is a Chinese-language router skill for the zmm skill family, helping an agent guide content creators and small business operators through onboarding, pre-task skill selection, and post-task navigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill as the public entry point for the zmm content and business workflow family. It routes requests to appropriate downstream skills, generates ready-to-send prompts, and provides guided onboarding or next-step navigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local discovery script can expose installed zmm skill names and filesystem paths to the agent context.

Mitigation: Review the discovery output before sharing transcripts or logs, and avoid installing the skill where local path disclosure would reveal sensitive workspace structure.

Risk: Downstream zmm skills may read configured vault paths or write drafts and memory when their workflows call for it.

Mitigation: Configure vault paths deliberately, review downstream skill permissions, and keep sensitive private material outside configured workflow directories unless it is needed.

Risk: Routing guidance can send a user to an unsuitable downstream skill if the request is ambiguous.

Mitigation: Use the skill's choice-question flow for missing information and verify the recommended downstream skill before executing follow-on work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [家族公约](references/家族公约.md)
- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [认知框架](references/认知框架.md)
- [实证规律库](references/实证规律库.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown routing recommendation with ready-to-send prompt text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include numbered next-step options and references to downstream zmm skills.]

## Skill Version(s):

0.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
