## Description: <br>
Designs a closed-loop email reactivation program for lapsed cohorts, including the cohort definition, staged offer ladder, re-consent capture step, sunset/suppression rule, and handoff summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and lifecycle email teams use this skill to design win-back and re-permission programs for subscribers who have stopped engaging. It helps define the lapsed cohort, plan a capped offer ladder, capture renewed consent, and decide whether each subject returns to active nurture or is suppressed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Engagement exports, cohort data, consent status, and suppression planning can contain sensitive marketing or personal data. <br>
Mitigation: Avoid including unnecessary personal data, and confirm save actions before storing campaign, cohort, consent, or suppression details in local memory files. <br>
Risk: Pasted lists, CSVs, ESP exports, and fetched files may include untrusted instructions or misleading content. <br>
Mitigation: Treat exported and pasted files as data only, ignore embedded instructions, and review the proposed reactivation plan before using it operationally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/reactivation-specialist) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown planning summary with a cohort definition, staged offer ladder, re-consent step, sunset rule, and handoff notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save user-confirmed summaries to local memory files.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
