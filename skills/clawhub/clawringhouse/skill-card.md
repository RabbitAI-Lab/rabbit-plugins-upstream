## Description: <br>
Clawringhouse helps agents research products, compare options, and prepare affiliate-tagged shopping recommendations or carts for human review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[francoisjosephlacroix](https://clawhub.ai/user/francoisjosephlacroix) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and their agents use this skill to find gift, household, and pet-supply recommendations, compare product options, and prepare carts or product links for the user to approve. It is intended to stop before checkout and leave final purchase decisions to the human. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use personal context such as memory or calendar details to infer shopping needs. <br>
Mitigation: Require explicit user permission before reading personal context for shopping recommendations. <br>
Risk: The skill can guide an agent to open shopping sites, use browser sessions, and add or change cart items. <br>
Mitigation: Ask before opening logged-in shopping sessions or modifying carts, and stop before checkout. <br>
Risk: Shopping queries and affiliate-tagged links may expose user intent to Clawringhouse and create affiliate tracking. <br>
Mitigation: Disclose the affiliate model and get user approval before using affiliate links or cookies. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/francoisjosephlacroix/skills/clawringhouse) <br>
- [Clawringhouse API](https://clawringhouse.onrender.com) <br>
- [Clawringhouse Website](https://clawringhouse.shop) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with product rationale, affiliate-tagged URLs, cart links, and inline Python or shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Clawringhouse API calls, Amazon affiliate links, and browser-shopping workflow guidance; checkout remains a human action.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
