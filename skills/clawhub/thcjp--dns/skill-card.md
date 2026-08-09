## Description: <br>
This skill helps agents analyze DNS records, plan TTL migrations, configure SPF, DKIM, DMARC, and CAA records, and troubleshoot Cloudflare proxy and resolver behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and site reliability engineers use this skill to plan DNS migrations, diagnose resolver and authoritative-record differences, and prepare DNS, mail-authentication, CAA, and Cloudflare configuration guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad agent powers and includes unclear automation, callback, messaging, file, API, and command capabilities beyond narrowly scoped DNS troubleshooting. <br>
Mitigation: Install only after review, allow only DNS-related commands that an operator approves, and avoid callback, messaging, file-write, or automated DNS-change features unless the publisher documents scope, destinations, confirmation steps, and rollback behavior. <br>
Risk: Broad DNS provider credentials or API keys could enable unintended DNS changes or disclosure. <br>
Mitigation: Use least-privilege, DNS-scoped credentials only when required, prefer manual approval for changes, and do not provide broad API keys to routine troubleshooting sessions. <br>
Risk: Incorrect DNS, mail-authentication, CAA, TTL, or Cloudflare guidance can cause outages, delivery failures, or certificate issuance problems. <br>
Mitigation: Review proposed record changes before applying them, stage TTL-sensitive migrations, verify authoritative and public resolver responses, and keep rollback records for changed DNS entries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with DNS record examples, diagnostic command snippets, and structured JSON-style result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include resolver comparison steps, DNS record snippets, troubleshooting checklists, and safety notes for manual review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
