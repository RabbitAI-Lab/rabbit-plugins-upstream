## Description: <br>
When the user wants multiple expert perspectives on a marketing question, this skill convenes a simulated board of marketing advisors, applies their documented frameworks, surfaces disagreements, and synthesizes a recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, founders, and operators use this skill to pressure-test marketing decisions through simulated expert perspectives. It is intended for strategy review, positioning, offers, pricing, brand, copy, content, paid media, launch, and channel-choice questions where disagreement and synthesis are useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local product-marketing context files when present, which can expose sensitive strategy or customer information to the agent session. <br>
Mitigation: Review local marketing context files before use and remove secrets or confidential details that should not be considered by the agent. <br>
Risk: Persona-style marketing advice can be mistaken for a real person's endorsement or direct review. <br>
Mitigation: Keep the simulation disclaimer, avoid invented endorsements, and ground each advisor take in the provided dossier or cited research. <br>
Risk: Live research for current marketing claims can introduce stale, weak, or uncited claims. <br>
Mitigation: Use current sources for time-sensitive questions, cite research-backed updates, and decline to attribute recent positions when sources are unavailable. <br>
Risk: User-directed custom advisor creation persists local Markdown files and could encode unsupported claims about private people. <br>
Mitigation: Create custom advisor dossiers only from user-supplied positions, store them in the requested local advisor path, and have the user review the dossier before relying on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/coreyhaines31/skills/marketing-council) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Evaluation Scenarios](artifact/evals/evals.json) <br>
- [Advisor Template](artifact/references/advisor-template.md) <br>
- [Alex Hormozi Advisor Dossier](artifact/references/advisors/alex-hormozi.md) <br>
- [Ann Handley Advisor Dossier](artifact/references/advisors/ann-handley.md) <br>
- [April Dunford Advisor Dossier](artifact/references/advisors/april-dunford.md) <br>
- [Byron Sharp Advisor Dossier](artifact/references/advisors/byron-sharp.md) <br>
- [Claude Hopkins Advisor Dossier](artifact/references/advisors/claude-hopkins.md) <br>
- [David Ogilvy Advisor Dossier](artifact/references/advisors/david-ogilvy.md) <br>
- [Eugene Schwartz Advisor Dossier](artifact/references/advisors/eugene-schwartz.md) <br>
- [Gary Halbert Advisor Dossier](artifact/references/advisors/gary-halbert.md) <br>
- [Gary Vaynerchuk Advisor Dossier](artifact/references/advisors/gary-vaynerchuk.md) <br>
- [Rory Sutherland Advisor Dossier](artifact/references/advisors/rory-sutherland.md) <br>
- [Russell Brunson Advisor Dossier](artifact/references/advisors/russell-brunson.md) <br>
- [Seth Godin Advisor Dossier](artifact/references/advisors/seth-godin.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown advisory session with optional local Markdown advisor dossier files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should identify the session as simulation, avoid fabricated quotes or endorsements, include disagreement mapping, and provide a chair's synthesis with next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
