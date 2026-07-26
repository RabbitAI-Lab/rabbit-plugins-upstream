## Description: <br>
Turn stakeholder feedback into agent work packets so an OpenClaw agent can read visual pins, implement fixes, and resolve the feedback loop. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcooley8](https://clawhub.ai/user/jcooley8) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to connect stakeholder visual feedback from live, staging, or local web pages to an OpenClaw agent workflow. It helps the agent configure Pincushion, retrieve actionable pins, claim work, make fixes, and resolve feedback with implementation metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pins and cloud sync can expose page URLs, screenshots, DOM snippets, selectors, comments, and acceptance criteria to Pincushion. <br>
Mitigation: Confirm Pincushion is approved to receive that data before enabling cloud sync; prefer local-only mode or staging use unless cloud sync is explicitly needed. <br>
Risk: The hosted no-install widget inspects pages and may be added to deployed sites. <br>
Mitigation: Review the hosted widget through the organization's security and privacy process before adding it to production pages. <br>


## Reference(s): <br>
- [Pincushion homepage](https://pincushion.io) <br>
- [Pincushion documentation](https://pincushion.io/docs) <br>
- [ClawHub skill page](https://clawhub.ai/jcooley8/skills/pincushion) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash, JSON, and HTML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node or npx. Cloud sync is optional and uses PINCUSHION_LICENSE_KEY or a project .feedback/.license-key file when enabled.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
