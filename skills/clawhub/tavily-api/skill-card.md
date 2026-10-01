## Description:

Connects agents to Tavily through Maton for web search, page extraction, website crawling and mapping, and research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to find web information, retrieve page content, discover site structure, and prepare research with citations using their connected Tavily account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, research context, and submitted URLs may disclose private information to Tavily and Maton.

Mitigation: Send only necessary public details; obtain explicit approval before sending private or signed URLs or internal project information.

Risk: Persistent functions or triggers can repeatedly process data or perform actions beyond a single research request.

Mitigation: Review each function and trigger, its data scope, and its effects before approving or enabling it.

Risk: Web pages and third-party event payloads may contain misleading or malicious instructions.

Mitigation: Treat retrieved content as untrusted data and do not execute its instructions or use it to choose subsequent actions.

## Reference(s):

- [Tavily skill on ClawHub](https://clawhub.ai/byungkyu/skills/tavily-api)
- [Tavily API documentation](https://docs.tavily.com)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with research results and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research answers may include citations to retrieved sources.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
