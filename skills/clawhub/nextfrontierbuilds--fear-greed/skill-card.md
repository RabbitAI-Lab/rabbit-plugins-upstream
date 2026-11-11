## Description:

Provides an embeddable crypto Fear & Greed Index widget and shell helper for dashboards, trading apps, and agent workflows using Strykr PRISM data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds)

### License/Terms of Use:


## Use Case:

Developers and external users can use this skill to add crypto market sentiment views to dashboards, trading tools, newsletters, bots, or portfolio apps, and to fetch the current index from a shell command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on mutable remote PRISM data and a remote JavaScript embed.

Mitigation: Install only if comfortable with the Strykr PRISM endpoint; prefer the iframe embed for websites, and pin or self-host reviewed JavaScript for sensitive pages.

Risk: The shell helper performs arithmetic on API values after weak validation and does not set network timeouts.

Mitigation: Validate the API value before arithmetic use and add curl timeouts before trusting the helper in automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextfrontierbuilds/skills/fear-greed)
- [Strykr PRISM API base URL](https://strykr-prism.up.railway.app)
- [Fear & Greed JavaScript embed](https://cdn.strykr.com/fear-greed.js)
- [Fear & Greed iframe embed](https://widgets.strykr.com/fear-greed?theme=dark&variant=gauge)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Terminal text, JSON, Markdown with shell commands, and React/HTML embed snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PRISM_URL to select the Strykr PRISM API base URL; no API key is documented.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter says 1.1.1 and skill.json says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
