## Description:

Helps authorized site owners manage LinkBunny backlink assignments, including profile setup, check-ins, contextual nofollow placements, reports, and rejections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkbunny](https://clawhub.ai/user/linkbunny)

### License/Terms of Use:

MIT-0

## Use Case:

External site owners and their authorized agents use this skill to operate LinkBunny backlink workflows for owned sites, including site registration, assignment review, publication approval support, and completion or rejection reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A LinkBunny API token could be exposed through chat, logs, screenshots, source files, or committed configuration.

Mitigation: Store the token only in an owner-approved private secret store and never print, log, paste, screenshot, or commit it.

Risk: An agent could take account, billing, credential, site registration, check-in, publication, report, or rejection actions without fresh owner authorization.

Mitigation: Require specific action-time owner approval for each sensitive workflow step, with bounded approval only when the owner explicitly grants it.

Risk: A backlink placement could be irrelevant, hidden, template-wide, outside the approved inventory, or missing the required nofollow attribute.

Mitigation: Inspect the owned corpus, stay within the returned inventory boundary, use truthful contextual placement, include rel="nofollow", and reject unsuitable assignments.

Risk: Self-reported LinkBunny completion could be mistaken for independent verification or a promise of search ranking, traffic, timing, or permanence.

Mitigation: Describe reports as self-reported records and avoid claims of independent verification, search-policy safety, or guaranteed SEO outcomes.

## Reference(s):

- [LinkBunny Agent Documentation](https://getlinkbunny.com/docs/agents?ref=clawhub)
- [LinkBunny Skill Source](https://getlinkbunny.com/skill.md)
- [ClawHub LinkBunny Skill Page](https://clawhub.ai/linkbunny/skills/linkbunny)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands and API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires owner-approved LinkBunny API token handling and action-time approval before site, billing, publication, report, or rejection actions.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
