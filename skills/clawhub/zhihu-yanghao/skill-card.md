## Description:

Automates a logged-in Zhihu account-nurturing workflow that helps an agent select topics, draft and publish answers or moments, verify results, and perform configured engagement actions through ego-browser.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a configurable Zhihu growth routine for a logged-in account, including topic rotation, answer generation, answer or moment publication, result verification, and optional engagement actions. It is intended for users who deliberately accept the operational and account-policy risks of automating public Zhihu activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, like, follow, collect, comment, or edit through a logged-in Zhihu account.

Mitigation: Review every generated post or edit before publication, keep dry-run defaults enabled until manually checked, and run only from an account and environment where this automation is intentional.

Risk: The workflow requires sandboxing to be disabled for ego-browser IPC, increasing local machine exposure.

Mitigation: Run it only in a disposable or tightly controlled environment, avoid machines with sensitive files, and re-enable sandboxing after the task finishes.

Risk: Automated engagement and anti-abuse evasion behavior may violate Zhihu rules or trigger account restrictions.

Mitigation: Follow the documented rate limits, keep higher-risk comment automation disabled unless explicitly needed, reduce the schedule if restrictions occur, and stop rather than retry when publishing appears stuck.

Risk: Parameter files in shared temporary paths can expose content or cause the wrong action to run.

Mitigation: Use isolated local paths for parameter and content files, inspect them before execution, and remove stale temporary files after each run.

## Reference(s):

- [Risk Control](references/risk-control.md)
- [Workflow](references/workflow.md)
- [Selectors](references/selectors.md)
- [Topic Strategy](references/topic-strategy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript snippets, JSON configuration, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local text drafts, parameter JSON files, and run logs depending on the workflow path.]

## Skill Version(s):

1.3.6 (source: server release metadata, target metadata, and skill title)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
