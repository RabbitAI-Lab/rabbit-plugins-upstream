## Description:

Static site deployment assistant for validating local build artifacts and guiding deployment to CloudStudio Sandbox, EdgeOne Pages, Netlify, Vercel, and GitHub Pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to validate static site build outputs, choose an appropriate deployment target, publish the site, and verify the resulting URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning script can persist local history, errors, preferences, and notes in skill directories.

Mitigation: Avoid recording secrets, internal URLs, credentials, or incident details in notes; remove or disable the learning script if persistent tracking is not required.

Risk: Static deployment may unintentionally publish sensitive files included in a build output directory.

Mitigation: Run the deployment checker and review flagged files such as .env, credentials, private keys, PEM files, and key.json before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/static-deploy)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include deployment target recommendations, validation checklists, and post-deployment verification steps.]

## Skill Version(s):

1.0.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
