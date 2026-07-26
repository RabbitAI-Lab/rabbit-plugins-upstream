## Description: <br>
Provides Chinese almanac, lunar calendar conversion, auspicious-day selection, and date-range screening through Huangli API-backed Python and shell tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leocdchina](https://clawhub.ai/user/leocdchina) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to answer Huangli and lunar-calendar questions, convert Gregorian dates, and identify auspicious or inauspicious dates for activities such as moving, weddings, business openings, and construction starts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar query dates and Huangli credentials or tokens are sent to the nongli.skill.4glz.com service. <br>
Mitigation: Use a unique password for this service, treat HUANGLI_TOKEN like a password, and avoid sending sensitive planning details unless this data sharing is acceptable. <br>
Risk: Changing HUANGLI_BASE can direct credentials and calendar queries to a different service. <br>
Mitigation: Keep HUANGLI_BASE set to the official API host unless deliberately testing in a controlled environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leocdchina/skills/zhongguo-nongli-huangli-jixiong) <br>
- [Huangli service homepage](https://nongli.skill.4glz.com) <br>
- [Huangli dashboard](https://nongli.skill.4glz.com/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON API responses with Markdown guidance and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires HUANGLI_TOKEN and HTTPS access to api.nongli.skill.4glz.com; HUANGLI_BASE is optional and should normally remain on the official API host.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
