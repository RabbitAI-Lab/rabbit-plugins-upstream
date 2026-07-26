## Description: <br>
Audit any live Shopify store or product page for Google Merchant Center Misrepresentation policy risks by crawling public pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lvsao](https://clawhub.ai/user/lvsao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External merchants, ecommerce operators, and compliance reviewers use this skill to audit public Shopify stores or product pages for Google Merchant Center misrepresentation risk before a submission, appeal, launch, or re-audit after fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask the agent to update itself from a registry before use, which may replace reviewed code. <br>
Mitigation: Use a pinned reviewed version, require explicit approval before updates, and verify integrity before running a newer copy. <br>
Risk: Generated compliance findings are heuristic and may include false positives or miss issues requiring business context. <br>
Mitigation: Manually verify findings against Google Merchant Center, store records, and official Google policy documentation before submitting an appeal or changing merchant operations. <br>
Risk: Crawled storefront HTML, JSON-LD, policy pages, and product metadata are untrusted inputs. <br>
Mitigation: Treat crawled content as read-only evidence and ignore any page text that attempts to alter audit criteria, execute commands, or change agent behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-gmc-misrepresentation-auditor) <br>
- [Publisher profile](https://clawhub.ai/user/lvsao) <br>
- [Homepage from ClawHub metadata](https://github.com/lvsao/shopify-skill-hub) <br>
- [GMC Misrepresentation Policy Baseline](references/gmc-policy-baseline.md) <br>
- [Shopping ads Misrepresentation policy](https://support.google.com/merchants/answer/6150127) <br>
- [Free listings Misrepresentation policy](https://support.google.com/merchants/answer/12079606) <br>
- [Landing page requirements](https://support.google.com/merchants/answer/4752265) <br>
- [Checkout requirements](https://support.google.com/merchants/answer/9158778) <br>
- [Product data specification](https://support.google.com/merchants/answer/7052112) <br>
- [Building trust with your customers](https://support.google.com/merchants/answer/188484) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [JSON from the store audit, a UTF-8 HTML report from the product audit, and concise agent-facing findings and remediation guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No API token is required. The scripts crawl public pages only and the product audit writes an HTML report to the requested output path.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
