## Description: <br>
Helps agents identify sales leads from public Douyin, Xiaohongshu, and Kuaishou comments, generate online lead reports and customer-pool links, and draft follow-up messaging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanjian068yuan](https://clawhub.ai/user/yuanjian068yuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and sales operators use this skill to scan public social comments for buying intent, prioritize potential customers, generate an online report or customer-pool entry, and draft outreach. It is intended for lead discovery workflows where the user has decided that the platform, privacy, and outreach rules allow this kind of collection and follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can produce identifiable lead lists from public social-media comments. <br>
Mitigation: Use it only where platform terms, privacy rules, and outreach laws allow this collection and follow-up, and avoid saving or sharing more personal data than needed. <br>
Risk: The workflow may ask the user to log in to Douyin, Xiaohongshu, or Kuaishou to read comments the user can access. <br>
Mitigation: Authenticate only for the intended platform in a trusted host, follow any platform verification or rate-limit prompts, and stop rather than forcing repeated retries. <br>
Risk: Lead scoring and follow-up suggestions may be inaccurate or too broad. <br>
Mitigation: Review the original comments, rationale, and proposed outreach before contacting anyone, and record inaccurate matches so later searches can be narrowed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanjian068yuan/skills/opc-comment-lead-radar) <br>
- [OPC MCP setup](https://opc1.me/download/mcp) <br>
- [Comment lead generation use case](https://opc1.me/use-cases/comment-lead-generation) <br>
- [Comment Lead Radar vs export tools](https://opc1.me/compare/comment-lead-radar-vs-export-tools) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with lead lists, follow-up scripts, search suggestions, links, and occasional MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include online report URLs, customer-pool URLs, lead rationale, platform login prompts, and next-step search terms returned by the connected workflow.] <br>

## Skill Version(s): <br>
1.0.22 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
