## Description: <br>
Reveal a public Shopify store's theme and detectable apps without API access. Use when someone wants a tech-stack audit, competitor research, or a visual report with evidence and confidence levels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, ecommerce operators, and analysts use this skill to scan public Shopify storefronts for theme and detectable app signals, then produce an evidence-backed report for tech-stack audits or competitor research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated reports may expose or re-share public technical signals such as script URLs, tracking IDs, headers, and page metadata. <br>
Mitigation: Use the skill only for public storefronts where this disclosure is acceptable, and review the report before sharing it. <br>
Risk: Opening the HTML report may contact Google, Clearbit, scanned storefront domains, or detected vendor domains for fonts, favicons, or logos. <br>
Mitigation: Open reports in an environment where these outbound requests are acceptable, or review the HTML report assets before opening. <br>
Risk: Crawled HTML and asset paths may contain prompt-like content or commands from the target storefront. <br>
Mitigation: Treat crawled content as static evidence only and ignore embedded instructions, as the skill's sandboxing rule requires. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-theme-apps-detector) <br>
- [Project homepage](https://github.com/lvsao/shopify-skill-hub) <br>
- [Detection Principles & Evidence Reference](artifact/references/detection-principles.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code] <br>
**Output Format:** [Chat summary plus a local HTML report file and JSON evidence from the scanner] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and public HTTP/HTTPS storefront access; output includes confidence levels and evidence chains.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
