## Description:

AI-powered multi-agent framework comparison and selection assistant that analyzes use cases, compares LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, Strands Agents, and AutoGen, and generates architecture recommendations and starter code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, AI engineers, data scientists, product managers, and regulated-industry technology teams use this skill to choose multi-agent orchestration frameworks, design agent architectures, define guardrails and evaluation plans, estimate cost and capacity, and generate starter Python scaffolds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Framework capabilities and ecosystem details may become outdated or incomplete.

Mitigation: Treat the skill as a planning aid and verify current framework facts against official documentation before committing to a production architecture.

Risk: Generated starter code may include third-party tools, API-key handling, persistence, or observability patterns that are not ready for direct production use.

Mitigation: Review and test generated code before running it, apply secrets management, least-privilege tool access, logging, rate limits, retry controls, and human-review checkpoints.

Risk: Multi-agent workflows can produce incorrect, costly, or hard-to-debug outputs if tracing, loop limits, and evaluation gates are missing.

Mitigation: Require traceable intermediate steps, bounded review loops, evaluation datasets, rollback paths, and human review for high-stakes or low-confidence outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/ai-agent-orchestration-advisor)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration, shell commands]

**Output Format:** [Markdown guidance with tables, architecture notes, checklists, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include framework comparisons, architecture diagrams, guardrail plans, cost estimates, and starter code examples.]

## Skill Version(s):

3.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
