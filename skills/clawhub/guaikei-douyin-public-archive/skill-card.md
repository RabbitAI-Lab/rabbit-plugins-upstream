## Description:

This skill helps agents retrieve public Douyin data for keyword video search, creator post collection, comment retrieval, and real-time hot-list checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill for Douyin public-content research, including topic discovery, competitor account analysis, comment review, and trend monitoring. It is intended for structured analysis of public data, not publishing, editing, or downloading videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, Douyin URLs or IDs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and invoke it only where sharing those inputs with guaikei.com is acceptable, and keep the token in a protected environment variable.

Risk: Search, post, and comment results can be saved under the skill's logs directory and may contain comments, profiles, or business research.

Mitigation: Protect access to the logs directory, review retention needs, and delete logs that contain sensitive or unnecessary collected data.

Risk: The skill says video downloads are out of scope, but returned schemas include media URL fields described as play or download addresses.

Mitigation: Treat returned media URLs as sensitive references for analysis only, and avoid using the skill for video downloading or redistribution workflows.

Risk: Broad or ambiguous prompts can trigger large public-data collection runs.

Mitigation: Use explicit Douyin-specific prompts and narrow limits, keywords, account URLs, or video IDs before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-archive)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei token and help site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON from CLI stdout with operational guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be written to local logs; single requests can return up to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, constants.js, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
