## Description: <br>
Website Pickpocket helps clone static or dynamic websites into offline static copies or framework projects such as HTML, React, Vue, and Angular. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhenyangze](https://clawhub.ai/user/zhenyangze) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site operators use this skill to create offline website copies, migrate site structure into framework projects, or generate backup versions of sites they own or are authorized to copy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help clone websites and discusses authenticated crawling, which may create legal, privacy, or access-control risk if used without permission. <br>
Mitigation: Use it only on sites you own or are explicitly authorized to copy, and review crawl scope before execution. <br>
Risk: Session cookies or localStorage values may expose sensitive account tokens if placed in plaintext configuration. <br>
Mitigation: Avoid real session credentials in config files; use least-privilege test accounts and remove secrets before sharing outputs. <br>
Risk: Proxy or user-agent settings could be used to bypass site protections. <br>
Mitigation: Do not use proxy or user-agent settings to bypass protections without permission, and set tight page and depth limits. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/zhenyangze/website-pickpocket-skill) <br>
- [ClawHub skill page](https://clawhub.ai/zhenyangze/skills/website-pickpocket-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files] <br>
**Output Format:** [Markdown with inline bash, YAML, and project-structure examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may describe generated static assets or framework project files for HTML, React, Vue, Angular, Svelte, or Tailwind CSS.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
