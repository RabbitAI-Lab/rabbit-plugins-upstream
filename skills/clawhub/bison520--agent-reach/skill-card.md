## Description: <br>
Agent Reach routes internet research requests across search, social media, career, GitHub, web, RSS, video, podcast, and finance sources using platform-specific backends and retry guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bison520](https://clawhub.ai/user/bison520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to choose appropriate read/search commands for internet research across supported platforms and gather source material without posting or performing content-processing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may route queries through logged-in browser sessions, cookies, API keys, and third-party reader or AI services. <br>
Mitigation: Use it only for web research that can be shared with those services, and avoid raw cookies, private URLs, tokenized links, or sensitive media unless a secure handling plan is in place. <br>
Risk: Some documented GitHub commands can create repositories, issues, pull requests, forks, releases, or other repository mutations. <br>
Mitigation: Prefer read-only commands for research tasks and run write-capable GitHub commands only after the user explicitly asks to mutate a repository. <br>
Risk: Platform-specific tools that rely on logged-in sessions or scraping can trigger authentication, rate-limit, captcha, or account-risk conditions. <br>
Mitigation: Run the documented backend health check before use, follow platform-specific retry guidance, and limit request volume for authenticated or rate-limited platforms. <br>


## Reference(s): <br>
- [Agent Reach homepage](https://github.com/Panniantong/Agent-Reach) <br>
- [Search tools](references/search.md) <br>
- [Social media and communities](references/social.md) <br>
- [Career and recruiting](references/career.md) <br>
- [Developer tools](references/dev.md) <br>
- [Web reading](references/web.md) <br>
- [Video and podcasts](references/video.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and tool/API call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read/search focused; temporary outputs are directed to /tmp/ when artifact guidance calls for files.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
