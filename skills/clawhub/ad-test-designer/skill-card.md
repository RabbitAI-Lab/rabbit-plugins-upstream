## Description: <br>
Ad Test Designer helps agents design paid-ad creative, landing-page, and incrementality tests, then read out effect size, uncertainty, practical significance, guardrails, and owner-governed decisions from user-provided results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, growth operators, and agents use this skill to plan A/B/n or incrementality tests, calculate sample-size and duration assumptions, and interpret finished own-data test exports without letting statistical helpers choose business actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided ad exports or summaries can contain misleading instructions or business-action claims. <br>
Mitigation: Treat exported data as untrusted input and review the generated test design or read-out before acting on it. <br>
Risk: A statistical signal could be mistaken for automatic approval to promote, kill, or roll back an ad change. <br>
Mitigation: Apply only a precommitted owner-approved action rule; otherwise return decision: UNDECIDED. <br>
Risk: Saved memory could retain test details or approved actions the user did not intend to persist. <br>
Mitigation: Save memory only after the user explicitly approves the specific test design or read-out summary. <br>


## Reference(s): <br>
- [Publisher Profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Skill Page](https://clawhub.ai/aaron-he-zhu/skills/ad-test-designer) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Ad Test Design Guide](references/test-design-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown test design or read-out with tables, documented assumptions, calculated evidence, and a handoff summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sample-size or significance helper commands when available; memory summaries are written only after user approval.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
