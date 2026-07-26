## Description: <br>
Momentum Planner helps agents plan the T+1 to T+30 post-launch momentum window, including launch-moment scheduling, announcement-tier routing, relaunch assessment, spike-to-owned handoff briefs, and next Tier-1 moment spacing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, launch, and product teams use this skill to preserve post-launch momentum after the launch-week spike fades. It produces a dated T+1 to T+30 moment plan, routes upcoming releases by announcement tier, evaluates relaunch legitimacy, and prepares handoff briefs for owned-channel follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose memory saves for launch plans, launch events, and claims, which could preserve incorrect dates, tiers, or metrics if accepted without review. <br>
Mitigation: Require user confirmation before saving; label metrics as Measured, User-provided, or Estimated; mark claims that need sources; and route durable launch or claims records through authorized proposal requests. <br>
Risk: Analytics exports, changelogs, and community posts used as inputs may contain untrusted instructions or misleading launch signals. <br>
Mitigation: Treat imported or pasted material only as evidence, not instructions, and ask for missing launch state instead of assuming dates, tiers, or stage facts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/momentum-planner) <br>
- [Project homepage from metadata](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a dated launch-moment calendar, announcement-tier routing, relaunch verdict, spike-to-owned handoff briefs, next-moment spacing check, and optional save/proposal prompts after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
