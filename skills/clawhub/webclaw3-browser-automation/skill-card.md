## Description:

webclaw3 lets agents automate and scrape websites through the user's own logged-in Chrome session, then turn successful browser workflows into reusable local skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use webclaw3 to complete browser tasks that need a logged-in Chrome session, such as search, data extraction, form interaction, and content downloads. After a successful exploration, they can distill the workflow into a reusable local script skill for scheduled or repeated runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give a local agent broad control over a real logged-in Chrome profile.

Mitigation: Use a separate Chrome profile or test accounts, and avoid connecting admin, financial, or other high-impact accounts.

Risk: Local relay or CDP services can expose browser-control capability while they are running.

Mitigation: Start them only when needed, stop them after use, and keep access limited to the local machine.

Risk: Generated browser automation skills may preserve unsafe assumptions or interact with sensitive pages.

Mitigation: Review and scan generated skills before installing or scheduling them.

Risk: Access keys and uploaded site-knowledge can reveal sensitive operational context.

Mitigation: Treat access keys and site-knowledge as sensitive, and avoid sharing private account data or confidential page content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/webclaw3-browser-automation)
- [Publisher profile](https://clawhub.ai/user/fatmind)
- [webclaw3 product site](https://webclaw3.com)
- [README](artifact/README.md)
- [Using webclaw3 in Claude Code](artifact/docs/claude-code.md)
- [Using webclaw3 in workbuddy](artifact/docs/workbuddy.md)
- [Using webclaw3 in qoderwork](artifact/docs/qoderwork.md)
- [Inside the webclaw3 skill](artifact/docs/webclaw3-skill-intro.md)
- [Setup guide](artifact/references/setup.md)
- [Distillation guide](artifact/references/brief.md)
- [Repair guide](artifact/references/repair.md)
- [CDP fallback guide](artifact/references/cdp-fallback.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce reusable local browser automation skills after a successful exploration and user-confirmed requirements.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; artifact package.json states 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
