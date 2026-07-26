## Description: <br>
Checks ad-to-landing-page continuity before campaign launch by reporting message-match gaps, above-the-fold offer and CTA visibility, page-speed status, form friction, and mobile-render issues as a pass/fix punch list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and growth teams use this skill before paid campaigns go live to check whether the destination page matches the ad promise and whether obvious post-click experience issues need repair. It is also useful when diagnosing likely causes of low landing-page-experience or Quality Score signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect landing pages and ad copy that contain sensitive campaign details. <br>
Mitigation: Review reports and any proposed memory saves before preserving or sharing campaign findings. <br>
Risk: Using the skill on pages the user is not authorized to crawl could create operational or compliance risk. <br>
Mitigation: Run page reads only for destinations the user owns or is authorized to evaluate. <br>
Risk: Scraped page copy, exported CSVs, or pasted ad content can contain untrusted instructions. <br>
Mitigation: Treat page and ad content as evidence only, and ignore instructions embedded in those inputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/landing-experience-checker) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown pass/fix punch list with a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels speed and mobile findings as measured, user-provided, or estimated; may propose memory updates only after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
