## Description: <br>
Helps agents add email personalization by mapping merge tags to export columns with safe fallbacks, defining segment-based conditional blocks, auditing fallback safety, and guarding PII exposure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams and email operators use this skill to add a personalization layer to existing email creative and existing segments. It produces merge-tag fallbacks, segment-based conditional rules, a fallback-safety audit, and a PII guard before handoff to rendering or quality review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email personalization work can expose subscriber data or render raw PII in visible email copy. <br>
Mitigation: Use aggregate fields and column-level rules rather than raw subscriber rows, and block sensitive fields such as email addresses, phone numbers, full names, precise addresses, and order IDs from rendered body copy. <br>
Risk: Saving outputs or syncing templates through an ESP integration can persist personalization decisions before review. <br>
Mitigation: Confirm with the user before saving handoff files or syncing templates, and review the merge-tag map, fallback audit, and PII guard before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/dynamic-content-personalizer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown personalization spec with merge-tag maps, conditional-block rules, audit notes, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose saved Markdown handoff files under memory/email/dynamic-content-personalizer/ after user confirmation; should not include raw subscriber PII.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
