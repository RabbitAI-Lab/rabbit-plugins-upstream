## Description:

Automates a WaXiang browser workflow to log in when needed, find a named store, and start or open it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[randydai](https://clawhub.ai/user/randydai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations agents use this skill to start a specific WaXiang store by name, handling login state, paginated account lookup, and store-start confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls an authenticated WaXiang browser session and can start stores on the user's behalf.

Mitigation: Use a dedicated browser profile with minimal account access and confirm the target account and store name before running.

Risk: The skill opens a browser remote-debugging port with broad origin allowance.

Mitigation: Use an isolated profile and close the entire WaXiang browser process after the workflow completes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/randydai/skills/waxiang-store-open)
- [WaXiang account user administration](https://hao.waxiang.com/account/userAdmin)
- [WaXiang account management](https://hao.waxiang.com/account/accManage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown instructions with command snippets and final started=true/false status text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a target store name; may use optional browser path, username, password, port, and isolated user data directory.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
