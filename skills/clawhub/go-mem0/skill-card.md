## Description:

Guides Go developers using an unofficial client to access Mem0 Platform memories and other hosted resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the go-mem0 client to Go projects and implement authenticated access to Mem0 hosted memories, entities, and other Platform resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked API key could expose hosted Mem0 resources.

Mitigation: Read MEM0_API_KEY from the environment; never hardcode, commit, or log the key or authenticated requests.

Risk: Memory content, queries, and metadata may be sent to the hosted API beyond the intended scope.

Mitigation: Send only necessary data and scope requests to the intended user, agent, app, or run.

Risk: Deletion and changes to organizations, projects, members, or webhooks can alter hosted resources; profile jobs can consume credits.

Mitigation: Confirm requested changes and costs before acting, and limit operations to task-owned resources.

## Reference(s):

- [go-mem0 setup and reference](references/setup.md)
- [go-mem0 client repository](https://github.com/psyb0t/go-mem0)
- [go-mem0 ClawHub release](https://clawhub.ai/psyb0t/skills/go-mem0)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go and a Mem0 Platform API key are required to use the client.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
