## Description: <br>
Semrush enables an agent to query domain overview, organic keyword, and organic competitor data through an OOMOL-connected Semrush account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SEO practitioners, marketing analysts, and agents use this skill to retrieve Semrush domain metrics, organic keywords, and organic competitor data. It is suited for read-only search intelligence workflows that inspect each action schema before running connector calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Semrush access is mediated through OOMOL and the oo CLI. <br>
Mitigation: Use the skill only when the user is comfortable with that intermediary and has intentionally connected the relevant Semrush account. <br>
Risk: First-time setup can involve shell installer, login, connection, or billing steps. <br>
Mitigation: Run setup only after the matching CLI, authentication, connection, credential, or billing error occurs. <br>
Risk: Future connector actions may be marked write or destructive even though this release lists only read actions. <br>
Mitigation: Confirm the exact payload and effect before write actions, and get explicit approval before destructive actions. <br>


## Reference(s): <br>
- [Semrush homepage](https://www.semrush.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-semrush) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the oo CLI, OOMOL sign-in, and a connected Semrush account; listed actions are read-only in this release.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
