## Description: <br>
Strykr Qa Bot provides AI-powered QA automation for the Strykr trading platform, including pre-built tests for crypto, stocks, news, events, AI chat, PRISM API health checks, known issue tracking, screenshots, and Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and QA engineers use this skill to run regression, smoke, and site health tests against Strykr or authorized Strykr-like environments. It helps validate trading dashboard pages, signal cards, AI chat behavior, PRISM endpoints, navigation, screenshots, console errors, timing, and known issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automated browser tests may capture screenshots, console logs, reports, and timing data from the target environment. <br>
Mitigation: Run the skill only against Strykr or authorized Strykr-like environments, and handle generated artifacts as potentially sensitive. <br>
Risk: The skill depends on web-qa-bot to drive browser actions and test execution. <br>
Mitigation: Pin or review the web-qa-bot dependency before using the skill in CI or other automated release gates. <br>
Risk: The configured tests perform network access and browser interactions against the target Strykr application. <br>
Mitigation: Use approved test accounts, target URLs, and CI permissions, and avoid running tests against environments where automated interaction is not authorized. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nextfrontierbuilds/skills/strykr-qa-bot) <br>
- [Strykr Application](https://app.strykr.ai) <br>
- [web-qa-bot Peer Dependency](https://github.com/NextFrontierBuilds/web-qa-bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown reports, YAML test configuration, TypeScript helper code, shell commands, screenshots, console captures, timing metrics, and pass/fail/known-issue statuses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports and browser artifacts may contain environment-specific page content, console output, screenshots, and network health details.] <br>

## Skill Version(s): <br>
0.1.2 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
