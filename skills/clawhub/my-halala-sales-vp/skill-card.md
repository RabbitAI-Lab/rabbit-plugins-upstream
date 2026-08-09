## Description:

Owner-triggered private sales workflow that refreshes Qianlima login, collects small bid list/detail samples, and can optionally generate detail notes.

This skill is for research and development only.

## Publisher:

[rony99](https://clawhub.ai/user/rony99)

### License/Terms of Use:

MIT-0

## Use Case:

The skill owner uses this agent workflow on an owner-controlled host to refresh Qianlima/Yifangbao authentication, collect limited sales bid search results, retrieve selected details, and summarize outputs for private review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow authenticates to Qianlima/Yifangbao and stores a reusable login token locally.

Mitigation: Install only for the intended owner, keep the workdir private, store credentials in a mode-600 env file, and never print tokens, openids, cookies, or full env files.

Risk: The workflow downloads and retains bid list, detail, and attachment artifacts.

Mitigation: Use small collection limits, keep generated data under the private workdir, and review retention before sharing or archiving outputs.

Risk: Optional detail analysis can send collected content to an external model endpoint.

Mitigation: Leave analysis disabled unless explicitly needed, confirm the endpoint and token before enabling it, and avoid sending sensitive attachment text without review.

Risk: The release security verdict is suspicious because the workflow handles third-party auth, retained artifacts, and optional external analysis with incomplete disclosure.

Mitigation: Review the skill before deployment, avoid broad triggers, and update or pin dependencies to reviewed versions.

## Reference(s):

- [Internal contract notes](references/contract.md)
- [ClawHub skill page](https://clawhub.ai/rony99/skills/my-halala-sales-vp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON files]

**Output Format:** [Markdown guidance with inline shell commands and local JSON/file artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain owner-only and must not include credentials.]

## Skill Version(s):

1.1.1 (source: server release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
