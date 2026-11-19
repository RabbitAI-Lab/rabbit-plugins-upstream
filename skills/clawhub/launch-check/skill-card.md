## Description:

Check whether the current repository is ready to launch. Reads its public ScBee readiness score, shows the score and the three fixes worth the most, offers to make those fixes locally, and only if the human says yes, lists the project on ScBee. Use when someone asks "is this ready to launch?", "what should I fix before I ship?", or wants a launch checklist for this repo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmakt99](https://clawhub.ai/user/hmakt99)

### License/Terms of Use:

MIT-0

## Use Case:

Repository owners and developers use this skill to assess a public GitHub repository's launch readiness and review prioritized fixes. With explicit approval, it can apply local fixes or create a public ScBee listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review noted an unresolved reference to scbee-verify.txt.

Mitigation: Check whether that file is expected for the repository before using the listing workflow.

## Reference(s):

- [ScBee](https://scbee.vercel.app)
- [launch-check on ClawHub](https://clawhub.ai/hmakt99/skills/launch-check)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown with a readiness score, band, and prioritized fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May offer local changes and a public listing, each only after explicit human approval.]

## Skill Version(s):

1.0.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
