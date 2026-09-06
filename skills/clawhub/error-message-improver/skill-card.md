## Description:

Helps developers, support teams, SaaS operators, and users turn vague error messages into clearer guidance that explains what failed, why it failed, and what action to take next.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, SaaS operators, and end users use this skill to rewrite, review, and operationalize error messages so troubleshooting output explains the failure, likely cause, and next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit-invocation wording may route general debugging or support prompts into this skill automatically.

Mitigation: Review the invocation policy before deployment and narrow trigger wording or disable implicit invocation when a workspace needs tighter routing.

Risk: Suggested error-message changes can still be incomplete, misleading, or too revealing for a production product.

Mitigation: Review proposed messages against product facts, support policy, privacy requirements, and the stated success criteria before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/error-message-improver)
- [Requirement Plan](references/requirement-plan.md)
- [regex format implementation?](https://github.com/sourcemeta/jsonschema/issues/842)
- [Anidb is temporarily down, we should have a better error message](https://github.com/pystardust/ani-cli/issues/1893)
- [Two error-signalling conventions coexist](https://github.com/sysbiolab/RGraphSpace/issues/12)
- [Review reminders: allow scheduling exact alarms](https://github.com/ankidroid/Anki-Android/issues/21752)
- [error-messages](https://segmentfault.com/t/error-messages)
- [Zig: Pointer Stability for ArrayLists](https://news.ycombinator.com/item?id=49502293)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Code, Configuration, Shell commands]

**Output Format:** [Markdown with optional code, shell command, checklist, workflow, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces concise, human-facing troubleshooting artifacts and validation notes; it does not require external tools or credentials.]

## Skill Version(s):

0.20260906.40422 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
