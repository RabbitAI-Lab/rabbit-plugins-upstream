## Description:

Call third-party APIs through the Maton gateway using credentials for apps the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to read or update data in services connected to their Maton account, and to configure related API workflows and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API writes and hosted or local automations can change data or continue acting without a person present.

Mitigation: Use read-only actions by default; get explicit approval for each write or automation, confirm its target and scope, and review any event destination or handler before it runs.

Risk: The security scan has medium confidence because three referenced files were only partially inspected.

Mitigation: Review the relevant app reference files and granted permissions before relying on actions for those services.

## Reference(s):

- [Maton API Gateway on ClawHub](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API results, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Varies by task; includes text or JSON results, Markdown guidance, shell commands, and optional Python or JavaScript examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results and available actions depend on the connected app, account permissions, and API limits.]

## Skill Version(s):

1.2.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
