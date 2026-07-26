## Description: <br>
Configures and debugs nginx for reverse proxying, load balancing, SSL/TLS termination, caching, redirects, static file serving, TCP/UDP proxying, containers, and production operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to write, review, debug, and tune nginx configurations for reverse proxies, static sites, SSL/TLS termination, containers, TCP/UDP proxying, and production operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can remember nginx-related preferences and context under ~/Clawic/data/nginx/. <br>
Mitigation: Review local preference and memory files, and avoid storing sensitive operational details unless they are needed for future nginx assistance. <br>
Risk: Nginx configuration advice can affect live traffic when applied. <br>
Mitigation: Review proposed configuration, run nginx -t, inspect the effective configuration when needed, and reload only after validation succeeds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/nginx) <br>
- [Clawic skill page](https://clawic.com/skills/nginx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with nginx configuration snippets, shell commands, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local nginx preferences and memory stored under ~/Clawic/data/nginx/.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
