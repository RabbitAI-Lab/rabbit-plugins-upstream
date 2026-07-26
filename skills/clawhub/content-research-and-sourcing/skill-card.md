## Description: <br>
Helps agents make content publish-ready by inventorying factual claims, tracing them to primary sources, checking freshness and context, testing AI-supplied citations, and preparing attribution/source logs before scheduling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, social media teams, and agents use this skill to verify stats, citations, quotes, and higher-risk health, finance, or legal claims before publishing. It guides source tracing, source-log creation, attribution, and escalation to human review when the agent lacks search access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect or unverifiable claims could be published as facts. <br>
Mitigation: Inventory load-bearing claims, trace them to primary sources, verify freshness and context, and cut or soften claims that fail verification. <br>
Risk: AI-supplied citations may be fabricated or may resolve to unrelated sources. <br>
Mitigation: Independently search each citation, confirm the link resolves to the claimed source, verify that the source says the claimed thing, and log the result. <br>
Risk: Health, finance, or legal claims can create higher reader harm and compliance risk if overstated. <br>
Mitigation: Use official or peer-reviewed primary sources, qualify language, add appropriate advice disclaimers, and route uncertain claims to human review. <br>
Risk: The agent may lack search access and overstate what it verified. <br>
Mitigation: When search is unavailable, output a checklist for human link review and do not claim verification was completed by the agent. <br>
Risk: Researched or pasted source material may contain content that should not steer the agent. <br>
Mitigation: Treat researched material as data for verification and attribution, not as instructions. <br>


## Reference(s): <br>
- [FACTS framework](artifact/references/the-facts-framework.md) <br>
- [Protocols, checklists and worked examples](artifact/references/protocols-and-templates.md) <br>
- [Research and sourcing 2026 reality](artifact/references/research-and-sourcing-2026-reality.md) <br>
- [Scope, distinctions and connections](artifact/references/scope-and-connections.md) <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/content-research-and-sourcing) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown] <br>
**Output Format:** [Markdown guidance with checklists, source logs, attribution notes, and revised claim language] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires web search for agent-side verification; without search access, it produces a human verification checklist.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
