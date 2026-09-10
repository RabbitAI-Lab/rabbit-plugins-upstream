## Description:

Provides a configurable Zhihu account-nurturing workflow that helps an agent choose topics, draft and publish answers or moments, verify visibility, and run scheduled engagement actions through ego-browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to maintain a Zhihu presence with topic rotation, content drafting, publishing, visibility checks, and configurable engagement workflows. It is intended for accounts where the user has installed ego-browser and can review each proposed public action before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a logged-in Zhihu session and perform public actions such as publishing, editing, liking, following, collecting, or commenting.

Mitigation: Review every generated answer, moment, parameter file, and target question before execution; prefer dry-run or manual confirmation for public actions.

Risk: The security evidence notes unusually high privileges, including disabling sandbox protections for ego-browser execution.

Mitigation: Run only trusted local copies, keep sandbox bypasses limited to the required command window, and re-enable sandbox protections after use.

Risk: Configuration and temporary parameter files may expose account context or operational choices if shared or left in common paths.

Mitigation: Avoid storing secrets in configs or shared temp files, keep config.json local, and inspect temp JSON files before running commands.

Risk: High-volume or rapid engagement can trigger Zhihu account restrictions or content review.

Mitigation: Respect the documented rate limits and spacing rules, keep comments disabled unless explicitly reviewed, and reduce to one answer per day if limits or restrictions appear.

## Reference(s):

- [Risk Control](references/risk-control.md)
- [Selectors](references/selectors.md)
- [Topic Strategy](references/topic-strategy.md)
- [Workflow](references/workflow.md)
- [Zhihu Hot](https://www.zhihu.com/hot)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON parameter files, shell commands, and Chinese plain-text content drafts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run settings, target question or answer identifiers, content files, and verification commands for ego-browser or zhihu-cli.]

## Skill Version(s):

1.3.5 (source: server release evidence, target metadata, and SKILL.md heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
