## Description:

深知可信PPT helps agents create editable PowerPoint presentations from user materials or trusted search results, using constrained SVG converted to native PowerPoint objects and delivering source-verification reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dknownai](https://clawhub.ai/user/dknownai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and presentation authors use this skill to turn topics or existing work materials into editable PPTX decks for reports, training, policy briefings, and data presentations. When trusted search is enabled, the skill can add authority-backed source material and deliver accompanying verification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request a phone number and verification code to set up external search access.

Mitigation: Confirm that users receive a clear account setup explanation before installation or use, including what information is requested and why.

Risk: Search topics and generated presentation content may be sensitive when sent to the dknowc service.

Mitigation: Avoid using trusted search for confidential topics unless the user has approved the data flow and the organization permits that external service.

Risk: Generated files may be copied from the skill workspace to a host workspace.

Mitigation: Tell users where outputs are delivered and review generated PPTX and HTML reports before sharing them outside the workspace.

Risk: API keys or access credentials are handled during setup.

Mitigation: Use temporary environment-based credentials when possible, do not expose full keys in conversation, and persist credentials only with explicit user approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dknownai/skills/dknownai-ppt-assistant)
- [DKnownAI publisher profile](https://clawhub.ai/user/dknownai)
- [dknowc open API endpoint](https://open.dknowc.cn/)
- [dknowc platform](https://platform.dknowc.cn/)
- [ppt-master upstream notice](https://github.com/hugohe3/ppt-master)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated presentation files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces editable .pptx files and, when trusted search is used, HTML provenance reports.]

## Skill Version(s):

1.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
