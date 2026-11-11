## Description:

Zhihu Yanghao Pkg helps agents run a configurable Zhihu account-nurturing workflow through ego-browser, including topic selection, answer drafting and publishing, engagement actions, moments, and verification steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage a logged-in Zhihu account with a scheduled account-growth routine. It guides and automates answer publishing, moments, engagement actions, and verification around a user-configured topic strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates a logged-in Zhihu account and can publish, edit, like, follow, collect, or comment publicly.

Mitigation: Use an isolated or low-privilege environment, keep dry-run modes enabled where available, and review content before public actions.

Risk: The workflow asks users to disable sandbox protections for ego-browser commands.

Mitigation: Run only when the operator accepts that trust boundary change, and re-enable sandbox protections after the task completes.

Risk: Account-growth and anti-detection behavior may violate platform rules or trigger account limits.

Mitigation: Follow the documented rate limits, reduce activity when limits appear, and confirm the workflow is acceptable for the target account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/zhihu-yanghao)
- [README](artifact/README.md)
- [Workflow](artifact/references/workflow.md)
- [Risk controls](artifact/references/risk-control.md)
- [Selectors](artifact/references/selectors.md)
- [Topic strategy](artifact/references/topic-strategy.md)
- [Zhihu Hot](https://www.zhihu.com/hot)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, JavaScript helper scripts, and generated Zhihu answer or moment text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local parameter and content files, drive ego-browser browser automation, and require human review before public account actions.]

## Skill Version(s):

1.3.6 (source: server release evidence and artifact heading)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
