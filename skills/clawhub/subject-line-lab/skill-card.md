## Description: <br>
Subject Line Lab helps marketers generate and pre-score email subject-line and preheader variants for spam-trigger patterns, truncation risk, emoji use, and inbox preview quality before A/B testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and email operators use this skill to draft or evaluate 3-8 subject-line and preheader variants for promo, cold-outbound, and newsletter campaigns, then rank survivors before test design. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spam-trigger and truncation checks are heuristic guidance and do not guarantee inbox placement or deliverability. <br>
Mitigation: Treat pre-scores as estimated screening signals, not final verdicts, and run a full deliverability and authentication review before sending. <br>
Risk: The skill may inspect pasted subject lines, preheaders, optional campaign exports, or connector-provided email data supplied by the user. <br>
Mitigation: Provide only the data needed for the review, treat campaign exports as untrusted input, and approve memory saves only when those learnings should be retained. <br>
Risk: Generated subject lines can become misleading if they add unsupported statistics, discounts, scarcity, or personalization claims. <br>
Mitigation: Require explicit source support for factual claims and keep unsupported claims flagged or excluded from send-ready variants. <br>


## Reference(s): <br>
- [Spam Trigger Checklist](references/spam-trigger-checklist.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/subject-line-lab) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown tables and concise handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include labeled subject/preheader variants, heuristic pre-score cards, inbox previews, ranked survivors, and reasons for cuts.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
