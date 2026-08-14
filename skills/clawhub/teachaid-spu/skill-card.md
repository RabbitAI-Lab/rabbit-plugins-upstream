## Description:

Discover and use Slid Phi University (SPU) powered by the TEACHAiD engine — personal teacher, curriculum, school factory, bursar, and double-entry books. Dual doors for humans and agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ceedot-rock](https://clawhub.ai/user/ceedot-rock)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to discover and interact with Slid Phi University's live teaching, curriculum, financial-aid, accounting, and text-to-speech service endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects agents to a live third-party education and commerce service.

Mitigation: Avoid sending sensitive student, financial, or account information unless the service has been reviewed and trusted for the intended use.

Risk: The skill discusses fees, financial aid, accreditation-sensitive education claims, and commerce flows.

Mitigation: Independently verify fees, accreditation, and financial-aid claims before relying on them or presenting them to users.

Risk: Agents could overstate service capabilities or invent unsupported endpoints.

Mitigation: Use the documented discovery endpoint first and describe only public, live behavior supported by the service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ceedot-rock/skills/teachaid-spu)
- [Agent discovery](https://teachaid.fly.dev/api/agent)
- [Agents manifest](https://teachaid.fly.dev/agents.json)
- [LLMs reference](https://teachaid.fly.dev/llms.txt)
- [Full LLMs reference](https://teachaid.fly.dev/llms-full.txt)
- [Campus app](https://teachaid.fly.dev)
- [OpenClaw metadata](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and HTTP endpoint references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl for live third-party service discovery; no credential variables are declared in the skill.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
