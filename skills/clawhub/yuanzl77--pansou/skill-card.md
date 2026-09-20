## Description:

pansou helps agents search user-configured PanSou cloud-drive services for media, software, document, and other resource links, including concurrent searches across multiple configured sites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzl77](https://clawhub.ai/user/yuanzl77)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to configure PanSou service endpoints, run health checks, and search cloud-drive resource links from one or more trusted PanSou instances. It is intended for finding resources the user is allowed to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured PanSou services receive search terms and may reveal sensitive viewing or download interests.

Mitigation: Use only trusted PanSou services and avoid searches that expose sensitive or unauthorized activity.

Risk: Verification output can contain an authentication token.

Mitigation: Do not share verify output; rotate or remove stored tokens if output is exposed.

Risk: GET mode can place search terms and parameters in URLs and logs.

Mitigation: Prefer the default POST mode and use --get only when a trusted service requires it.

Risk: The skill broadly triggers searches for viewing or download links.

Mitigation: Use it only for resources the user is allowed to access and confirm ambiguous intent before searching.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzl77/skills/pansou)
- [CLI parameter reference](references/api-params.md)
- [Supported cloud-drive types](references/cloud-types.md)
- [PanSou GitHub project](https://github.com/fish2018/pansou)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown links, JSON search results, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Go and user-configured PANSOU_URL or PANSOU_URLS; default searches use POST and may authenticate against configured PanSou services.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
