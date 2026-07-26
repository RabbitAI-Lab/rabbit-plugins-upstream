## Description: <br>
Browser Agent Tool Free guides an agent through headless browser automation using accessibility-tree snapshots, ref-based element selection, session isolation, screenshots, PDF export, and network-aware waits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to automate multi-step browser workflows such as navigation, form filling, search result extraction, screenshots, PDF generation, and isolated session testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a browser, reuse login state, and perform account-affecting web actions. <br>
Mitigation: Install only when browser control is intended, and require explicit user approval before loading auth state, submitting forms, clicking account-affecting controls, or using logged-in accounts. <br>
Risk: Saved state files, cookies, screenshots, PDFs, and HAR-like outputs may contain sensitive information. <br>
Mitigation: Treat those artifacts as sensitive and limit storage, sharing, and retention to the current task need. <br>
Risk: The workflow depends on an external npm package and browser runtime. <br>
Mitigation: Verify the npm package and runtime requirements before installing globally. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/browser-agent-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce screenshots, PDFs, saved browser state files, extracted page content, execution logs, and structured JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
