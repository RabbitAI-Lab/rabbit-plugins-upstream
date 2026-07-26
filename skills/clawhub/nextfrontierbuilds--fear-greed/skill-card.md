## Description: <br>
Embeddable Fear & Greed Index for crypto dashboards with terminal, JSON, React, HTML, and iframe usage examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, dashboard builders, and agent users can fetch or embed crypto Fear & Greed sentiment data for trading dashboards, newsletters, portfolio tools, and market-sentiment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a third-party Strykr PRISM endpoint and optional hosted widget/CDN examples. <br>
Mitigation: Install only when the endpoint and hosted embeds are trusted, and review availability, privacy, and dependency expectations before production use. <br>
Risk: The shell script expects curl and jq to be available. <br>
Mitigation: Confirm these command-line tools are installed in the agent runtime before using the script. <br>
Risk: Broad market-sentiment triggers may activate the skill in contexts where crypto Fear & Greed data is not intended. <br>
Mitigation: Use more specific triggers or invocation guidance when deploying the skill in production agent workflows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/nextfrontierbuilds/skills/fear-greed) <br>
- [Strykr PRISM Fear & Greed Endpoint](https://strykr-prism.up.railway.app/market/fear-greed) <br>
- [Strykr Fear & Greed Widget CDN](https://cdn.strykr.com/fear-greed.js) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, JSON, JSX, HTML, iframe, and environment-variable examples; the bundled script can emit terminal text or raw JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses PRISM_URL to select the Strykr PRISM API base URL; the shell script requires curl and jq.] <br>

## Skill Version(s): <br>
1.1.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
