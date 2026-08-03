## Description: <br>
Helps agents verify content before publication by triaging factual claims, tracing sources, checking freshness and context, testing AI-supplied citations, and preparing attribution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content, marketing, and social-media teams use this skill to make drafts publish-ready by checking statistics, citations, quotes, and high-impact claims before scheduling. It is especially relevant for stat-heavy content, AI-assisted research, viral claims, and health, finance, or legal topics that need a higher sourcing bar. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may overstate verification when it lacks web search or source access. <br>
Mitigation: The skill instructs the agent to state what it could verify, write a human checklist for inaccessible sources, and avoid fabricating source-log entries or verification results. <br>
Risk: AI-supplied citations or inherited links may be fabricated, unrelated, stale, superseded, or retracted. <br>
Mitigation: Run the citation protocol: confirm the source exists, the link resolves to the claimed work, the source says what the draft claims, the source is current, and the result is logged. <br>
Risk: Health, finance, legal, and other high-impact claims can mislead readers if they rely on weak or outdated evidence. <br>
Mitigation: Use official or peer-reviewed primary sources, qualified language, appropriate disclaimers, and human review before scheduling public content. <br>


## Reference(s): <br>
- [The FACTS framework](artifact/references/the-facts-framework.md) <br>
- [Protocols, checklists & worked examples](artifact/references/protocols-and-templates.md) <br>
- [Scope, distinctions & connections](artifact/references/scope-and-connections.md) <br>
- [The reality of research & sourcing in 2026](artifact/references/research-and-sourcing-2026-reality.md) <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/content-research-and-sourcing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance, checklists, source-log tables, attribution notes, and claim-review recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No tool file; the skill guides agent behavior and asks for human link-checking when web search is unavailable.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
