## Description:

Provides browser automation designed to resist headless detection for authorized QA, compatibility testing, and defensive security research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized security testers use this skill to exercise their own sites or explicitly in-scope targets against anti-bot systems and investigate browser compatibility issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation can be used outside the authorized test scope.

Mitigation: Use only on owned systems or targets with written authorization; avoid real accounts and production data.

Risk: An exposed browser service can grant access to page data, cookies, and browser actions.

Mitigation: Bind the API and noVNC viewer to localhost, set AUTH_TOKEN, and use an authenticating proxy if remote access is necessary.

Risk: Automatically accepted dialogs or URL-triggered loaders can change site state unexpectedly.

Mitigation: Disable dialog auto-accept before stateful actions and review all loader YAML before mounting it.

Risk: Persistent browser profiles and broad page captures can expose sensitive session or page information.

Mitigation: Use isolated test accounts, collect only necessary content, and protect or remove persisted profiles after testing.

Risk: Running an unreviewed container image can introduce supply-chain exposure.

Mitigation: Review and pin the container image by digest before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/stealthy-auto-browse)
- [Setup and security guidance](references/setup.md)
- [Humanized input documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/api.md#humanized-input)
- [Script control-flow documentation](https://github.com/psyb0t/docker-stealthy-auto-browse/blob/main/docs/script-mode.md#control-flow)

## Skill Output:

**Output Type(s):** [Text, JSON, Images, Shell commands, Configuration instructions]

**Output Format:** [Browser action results and page text in JSON, screenshots as images, and setup guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can retain browser sessions across runs when a persistent profile is mounted.]

## Skill Version(s):

3.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
