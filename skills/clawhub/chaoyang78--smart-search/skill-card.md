## Description: <br>
Smart Search routes an agent's information requests through OpenCLI search sources based on the requested site, topic, language, and need for primary or vertical results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to guide an agent in selecting OpenCLI search sources for web, AI, social, technical, news, shopping, travel, hiring, finance, and Chinese-language information requests. It emphasizes live help checks, source-specific limits, and a short search summary for traceability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms may be sent to external AI, social, shopping, travel, media, or other search providers through OpenCLI. <br>
Mitigation: Avoid entering sensitive queries and specify the intended platform, language, or region when source choice matters. <br>
Risk: Search results can be incomplete, unavailable, rate limited, or less authoritative than primary sources. <br>
Mitigation: Use the required live OpenCLI help checks, track per-site calls, fall back to appropriate alternate sources, and state coverage gaps in the answer. <br>
Risk: AI search sources may provide summaries without enough primary evidence. <br>
Mitigation: Supplement AI output with one or two relevant vertical sources when the task needs original posts, videos, products, jobs, or authoritative corroboration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chaoyang78/skills/smart-search) <br>
- [AI default sources](artifact/references/sources-ai.md) <br>
- [Technical and academic sources](artifact/references/sources-tech.md) <br>
- [Social media sources](artifact/references/sources-social.md) <br>
- [Media and entertainment sources](artifact/references/sources-media.md) <br>
- [Information and knowledge sources](artifact/references/sources-info.md) <br>
- [Shopping sources](artifact/references/sources-shopping.md) <br>
- [Travel sources](artifact/references/sources-travel.md) <br>
- [Other vertical sources](artifact/references/sources-other.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, text] <br>
**Output Format:** [Markdown guidance with OpenCLI command examples and a search summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routes searches to external sources and requires per-site call tracking.] <br>

## Skill Version(s): <br>
4.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
