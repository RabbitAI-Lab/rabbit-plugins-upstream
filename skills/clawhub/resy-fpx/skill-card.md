## Description:

Query and act on Resy restaurant reservations from a shell using curl against api.resy.com, with fpx used only for one-time token bootstrap when credentials are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users use this skill to script Resy reservation workflows from an agent, including venue search, slot checks, booking or cancellation, favorites, Priority Notify, and account profile lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses sensitive Resy account tokens.

Mitigation: Treat RESY_TOKEN like a password, avoid committing or logging it, and refresh it only through the documented credential or browser bootstrap flow.

Risk: The curl examples can create or cancel real reservations and change favorites or Priority Notify subscriptions.

Mitigation: Review commands before execution and read back account state before and after write actions.

Risk: The browser-bridge bootstrap path uses an unpinned global install.

Mitigation: Prefer a pinned or local install for the browser bridge, and remove or unpair it after token bootstrap.

## Reference(s):

- [Resy API ready-to-run requests](references/resy-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and fpx command examples; no generated files are required.]

## Skill Version(s):

0.13.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
