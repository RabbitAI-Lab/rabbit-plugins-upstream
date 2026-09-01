## Description:

詹明明 is a Chinese-language routing skill that helps content creators and small business operators choose the right zmm-family skill, run guided onboarding, and produce a direct next-step prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and small business operators use this skill as the entry point for a zmm skill family. It routes content, publishing, review, retrospective, portfolio, revenue, concentration, dependency, and decision tasks to the appropriate downstream skill and returns a ready-to-send prompt rather than doing the downstream work itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect locally installed zmm-family skills and display real filesystem paths.

Mitigation: Install it only in workspaces where local skill names and paths are acceptable to expose in agent output.

Risk: The skill relies on configured vault and memory paths for account-specific work.

Mitigation: Review the configured memory and vault paths before using the skill with sensitive business, account, or creator data.

Risk: Routing guidance may send users to downstream skills that operate on drafts, business facts, or publishing decisions.

Mitigation: Use explicit /zmm commands, review generated prompts before forwarding them to downstream skills, and confirm redline checks before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [交互规范](references/交互规范.md)
- [内容理论底座](references/内容理论底座.md)
- [实证规律库](references/实证规律库.md)
- [家族公约](references/家族公约.md)
- [认知框架](references/认知框架.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown guidance with numbered options, ready-to-send prompts, and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-first responses with English support; routes to installed zmm-family skills and stops after producing a prompt unless onboarding mode applies.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
