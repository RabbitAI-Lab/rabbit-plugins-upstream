## Description: <br>
Creates and maintains OpenCLI agent-facing site sitemaps with navigation, page-state, action, workflow, API-reference, pitfall, and fallback knowledge for browser workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent authors use this skill to create compact, evidence-backed OpenCLI sitemaps that help browser agents navigate sites, choose adapters, recover from stale page knowledge, and preserve durable workflow context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent sitemap drafts and traces can expose sensitive internal URLs, private workflows, or account-specific details if promoted without review. <br>
Mitigation: Review and clean ~/.opencli/sites/<site>/sitemap/ and related traces before promotion; redact secrets, private identifiers, private messages, cookies, and account-specific values. <br>
Risk: Stale sitemap entries can mislead agents when current browser state differs from recorded navigation or action guidance. <br>
Mitigation: Treat browser state as authoritative, mark conflicting entries stale, and keep actions tied to observed OpenCLI browser evidence before promotion. <br>
Risk: Overly broad or brittle selectors can cause agents to click the wrong element or rely on unstable page structure. <br>
Mitigation: Use stable semantic anchors, scoped partial selectors, and recovery instructions; avoid snapshot indices, single-class selectors, and unverified paths. <br>
Risk: Sitemaps could accidentally document bypasses for CAPTCHA, WAF, access control, rate limits, or paid gates. <br>
Mitigation: Reject sitemap entries that describe bypass behavior and keep recovery guidance limited to legitimate navigation, verification, and fallback paths. <br>


## Reference(s): <br>
- [Sitemap Schema Reference](references/sitemap-schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/chaoyang78/skills/opencli-sitemap-author) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown sitemap files with YAML frontmatter, compact YAML action blocks, and inline OpenCLI command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local sitemap drafts before promotion and uses browser evidence, stale markers, and adapter health notes to keep guidance reviewable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
