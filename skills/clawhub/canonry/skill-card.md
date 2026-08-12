## Description:

Canonry helps agents set up and operate AEO projects by measuring brand mentions and citations across AI answer engines, diagnosing regressions, running technical audits, and acting through the Canonry CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arberx](https://clawhub.ai/user/arberx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and SEO/AEO operators use Canonry to monitor AI answer-engine visibility for websites, diagnose mention or citation regressions, audit technical SEO/AEO issues, and coordinate approved changes across integrations such as Search Console, WordPress, traffic sources, and ads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Canonry operations, including write-capable workflows and spend-capable ads actions.

Mitigation: Use read-only or project-scoped keys where possible, require explicit approval for each sweep or mutation, and manually review ads grants, activation steps, and budgets before execution.

Risk: Canonry configuration may contain private API keys and project access details.

Mitigation: Keep ~/.canonry/config.yaml private, do not paste or print credentials in agent chat or shared logs, and avoid storing the config in repositories.

Risk: Live WordPress or site changes could affect production content.

Mitigation: Use dry runs and staging workflows first, then require explicit approval before pushing changes live.

## Reference(s):

- [Canonry Skill Page](https://clawhub.ai/arberx/skills/canonry)
- [Canonry Website](https://canonry.ai)
- [Canonry Documentation](https://github.com/Canonry/canonry)
- [AINYC AEO Methodology](https://ainyc.ai/aeo-methodology)
- [AEO Analysis](references/aeo-analysis.md)
- [Canonry CLI](references/canonry-cli.md)
- [Google Business Profile](references/google-business-profile.md)
- [Indexing Workflows](references/indexing.md)
- [Server-Side Traffic](references/server-side-traffic.md)
- [WordPress Integration](references/wordpress-integration.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

4.157.0+9318464 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
